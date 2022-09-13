from print_reverse_linked_list import Solution


def test_empty_linked_list_iterative(create_empty_linked_list, capfd):
    solution = Solution()
    solution.reverse_linked_list_iterative(create_empty_linked_list)
    out, err = capfd.readouterr()
    assert out == ""


def test_empty_linked_list_recursive(create_empty_linked_list, capfd):
    solution = Solution()
    solution.reverse_linked_list_recursive(create_empty_linked_list)
    out, err = capfd.readouterr()
    assert out == ""


def test_linked_list_with_one_item_iterative(create_linked_list_with_one_item, capfd):
    solution = Solution()
    solution.reverse_linked_list_iterative(create_linked_list_with_one_item)
    out, err = capfd.readouterr()
    assert out == "1\n"


def test_linked_list_with_one_item_recursive(create_linked_list_with_one_item, capfd):
    solution = Solution()
    solution.reverse_linked_list_recursive(create_linked_list_with_one_item)
    out, err = capfd.readouterr()
    assert out == "1\n"


def test_linked_list_iterative(create_linked_list, capfd):
    solution = Solution()
    solution.reverse_linked_list_iterative(create_linked_list)
    out, err = capfd.readouterr()
    assert out == "5\n4\n3\n2\n1\n"


def test_linked_list_recursive(create_linked_list, capfd):
    solution = Solution()
    solution.reverse_linked_list_recursive(create_linked_list)
    out, err = capfd.readouterr()
    assert out == "5\n4\n3\n2\n1\n"
