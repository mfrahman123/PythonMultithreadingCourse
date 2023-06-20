import concurrent.futures

def sort_toy(toy):
    # Sorting logic here
    return sorted(toy)

def main():
    toys = [4, 2, 6, 1, 3, 5]  # Toy numbers to sort

    # Using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Each friend (thread) sorts a portion of the toys simultaneously
        results = [executor.submit(sort_toy, (toy,)) for toy in toys]

        print("Sorted toys using ThreadPoolExecutor:")
        for result in concurrent.futures.as_completed(results):
            sorted_toy = result.result()
            print(sorted_toy)

    # Using ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Each friend (process) sorts their own portion of the toys independently
        results = [executor.submit(sort_toy, (toy,)) for toy in toys]

        print("Sorted toys using ProcessPoolExecutor:")
        for result in concurrent.futures.as_completed(results):
            sorted_toy = result.result()
            print(sorted_toy)

if __name__ == '__main__':
    main()

