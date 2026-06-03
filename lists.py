def main():
    my_list = ["apple", "banana", "cherry"]
    print("Initial list:", my_list)
  
    my_list.append("date")
    print("After appending 'date':", my_list)
    print(my_list[1:3])
    my_list.remove("banana")
    print("After removing 'banana':", my_list)
    my_list.insert(1, "blueberry")
    print("After inserting 'blueberry' at index 1:", my_list)
    print("List length:", len(my_list))
    print("First item:", my_list[0])
    print("Last item:", my_list[-1])

    my_list.extend(["elderberry", "fig", "grape"])
    print("After extending the list with more fruits:", my_list)
    my_list.sort()
    print("After sorting the list:", my_list)

if __name__ == "__main__":
    main()