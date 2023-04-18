import xml.etree.ElementTree as ET

library = ET.Element("library")

book1 = ET.SubElement(library, "book")
title1 = ET.SubElement(book1, "title")
title1.text = "Bahuballi"
author1 = ET.SubElement(book1, "author")
author1.text = "Rajamouli"
year1 = ET.SubElement(book1,"Year")
year1.text="2016"

book2 = ET.SubElement(library, "book")
title2 = ET.SubElement(book2, "title")
title2.text = "Mockingbird"
author2 = ET.SubElement(book2, "author")
author2.text = "Jack Lee"
year2 = ET.SubElement(book2,"Year")
year2.text="2020"


book3 = ET.SubElement(library, "book")
title3 = ET.SubElement(book3, "title")
title3.text = "Avatar"
author3 = ET.SubElement(book3, "author")
author3.text = "James cameron"
year3 = ET.SubElement(book3,"Year")
year3.text="2020"


book4 = ET.SubElement(library, "book")
title4 = ET.SubElement(book4, "title")
title4.text = "Mission Impossible"
author4 = ET.SubElement(book4, "author")
author4.text = "Tom Crusie"
year4 = ET.SubElement(book4,"Year")
year4.text="2012"


tree = ET.ElementTree(library)

tree.write("books.xml")

