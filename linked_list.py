import unittest

from lab1221 import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_insert_after_value(self):
        llist = LinkedList()
        llist.insert_at_end(1)
        llist.insert_at_end(2)
        llist.insert_at_end(3)
        llist.insert_at_end(4)
        llist.insert_at_end(5)

        llist.insert_after_value(1, 10)
        llist.insert_after_value(3, 20)
        llist.insert_after_value(5, 30)

        expected_output = "1 10 2 3 20 4 5 30"
        actual_output = ""
        current = llist.head
        while current:
            actual_output += str(current.data) + " "
            current = current.next
        self.assertEqual(actual_output.strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
