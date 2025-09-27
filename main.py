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
while current is not None:
    print(current.book_name)
    current = current.next