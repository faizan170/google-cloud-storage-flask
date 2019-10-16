from utils import process_tree
from storage import list_blobs


mainPath = "codeframe@gmail.com/ie6gpd-pgq3fw-ia6k2c-syfkw0-39cz/y3gzkw-kkcpek-mzcmks-q7dh1f-701g/"
data = list_blobs(mainPath)

finalData = process_tree(data, mainPath)

print(finalData)