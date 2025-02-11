class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items is not None else []
        self.pageSize = int(pageSize)  # Convertit en entier si c'est un float
        self.currentPage = 1
        self.totalPages = max(1, (len(self.items) // self.pageSize))  # Calcul du nombre total de pages

    def getVisibleItems(self):
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]

    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
        return self  # Permet le chaînage

    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        pageNum = int(pageNum)  # Convertit en entier si c'est un float
        if pageNum < 1:
            self.currentPage = 1
        elif pageNum > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = pageNum
        return self

# Initialisation avec alphabetList
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

# Test des méthodes
def test_pagination(p):
    print("Page 1:", p.getVisibleItems())
    print("Page 2:", p.nextPage().getVisibleItems())
    print("Page 3:", p.nextPage().getVisibleItems())
    print("Page précédente:", p.prevPage().getVisibleItems())
    print("Dernière page:", p.lastPage().getVisibleItems())
    print("Première page:", p.firstPage().getVisibleItems())
    print("Aller à la Page 3:", p.goToPage(3).getVisibleItems())
    print("Aller à une page trop grande:", p.goToPage(10).getVisibleItems())
print(p.getVisibleItems())
print(p.nextPage())
print(p.getVisibleItems())
print(p.lastPage())
print(p.getVisibleItems())
print(p.totalPages)
print(p.goToPage(10))
print(p.goToPage(6))
print(p.goToPage(4))
print(p.getVisibleItems())
print(p.currentPage)
test_pagination(p)
