import urllib.request
import threading

# Global variables
urls = ['https://www.gutenberg.org/cache/epub/70992/pg70992.txt', 'https://www.gutenberg.org/cache/epub/70998/pg70998.txt', 'https://www.gutenberg.org/cache/epub/71000/pg71000.txt']
downloaded_files = []
lock = threading.Lock()

def download_file(url):
    # Extract the file name from the URL
    file_name = url.split('/')[-1]

    # Download the file
    print(f"Downloading {file_name}...")
    urllib.request.urlretrieve(url, file_name)

    # Acquire the lock to access the shared resource
    lock.acquire()

    # Add the downloaded file to the shared list
    downloaded_files.append(file_name)

    # Release the lock
    lock.release()

    print(f"{file_name} downloaded.")

def main():
    # Create thread for each URL
    threads = []
    for url in urls:
        t = threading.Thread(target=download_file, args=(url,))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Print the downloaded files
    print("\nDownloaded files:")
    for file in downloaded_files:
        print(file)

if __name__ == '__main__':
    main()
