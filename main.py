class Node:
    def __init__(self, book_name):
        self.book_name = book_name
        self.next = None
        self.prev = None


list_of_books = [
    "Genesis","Exodus","Leviticus","Numbers","Deuteronomy",
    "Joshua","Judges","Ruth","1 Samuel","2 Samuel",
    "1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra",
    "Nehemiah","Esther","Job","Psalms","Proverbs",
    "Ecclesiastes","Song of Songs","Isaiah","Jeremiah","Lamentations",
    "Ezekiel","Daniel","Hosea","Joel","Amos",
    "Obadiah","Jonah","Micah","Nahum","Habakkuk",
    "Zephaniah","Haggai","Zechariah","Malachi",
    "Matthew","Mark","Luke","John","Acts",
    "Romans","1 Corinthians","2 Corinthians","Galatians","Ephesians",
    "Philippians","Colossians","1 Thessalonians","2 Thessalonians","1 Timothy",
    "2 Timothy","Titus","Philemon","Hebrews","James",
    "1 Peter","2 Peter","1 John","2 John","3 John",
    "Jude","Revelation"
]

head = None
previous_node = None

for books in list_of_books:
    new_node = Node(books)
    if head is None:
        head = new_node
    if previous_node is not None:
        previous_node.next = new_node
        new_node.prev = previous_node
    previous_node = new_node
    
current = head
while True:
    user_input = input("Enter command:")

    if user_input == "current":
        if current.book_name is not None:
            print(current.book_name)
        else:
            print("You are not at a book.")
    elif user_input == "next":
        if current.next is not None:
            current = current.next
            print(current.book_name)
        else:
            print("You're at the last book, Can't go forward.")
    elif user_input == "prev":
        if current.prev is not None: 
            current = current.prev
            print(current.book_name)
        else:
            print("You are at the first book. Can't go backward")
    elif user_input.startswith("jump"):
        parts = user_input.split()
        if len(parts) > 1:
            book_name = parts[1]
            print(book_name)
    elif user_input == "quit":
        break
    else:
        print("Invalid input")