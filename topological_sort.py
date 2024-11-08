import networkx as nx
s = nx.DiGraph([("The Path to Power", "Means of Ascent"), ("Means of Ascent", "Master of the Senate"), ("Master of the Senate", "The Passage of Power"), 
     ("The Rise of Theodore Roosevelt", "Theodore Rex"), ("Theodore Rex", "Colonel Roosevelt"),
     ("Thomas Jefferson: The Art of Power", "And There Was Light: Abraham Lincoln and the American Struggle"),
     ("George Washington A life", "Grant"),
     ("A Promised Land", "My Life"), ("My Life", "Decision Points"),
     ("Thomas Jefferson: The Art of Power", "American Sphinx: The Character of Thomas Jefferson"),
     ("Truman", "1776"), ("The Path to Power", "A Promised Land")])
print(list(nx.topological_sort(s)))