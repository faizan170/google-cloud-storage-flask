import json, os
from storage import download_blob


def process_tree(data, mainPath):
    dataJ = {}
    for row in data:
        if row != "":
            d = []
            typeK = "folder" if row[-1] == "/" else "file"
            dataJ["/root/" + row] = {"path": "/root/" + row, "type" : typeK}
            if typeK == "folder":
                child = []
                for row1 in data:
                    if row1 != row and len(row1) > len(row):
                        if row == row1[:len(row)]:
                            row1C = row1.replace(row, "")
                            if len(row1C.split("/")) == 1:
                                child.append("/root/" + row1)
                            elif row1C.split("/")[1] == "" and len(row1C.split("/")) == 2:
                                child.append("/root/" + row1)
                dataJ["/root/" + row]["children"] = child
            else:
                filePath = "temp/" + row.split("/")[-1]
                download_blob(os.path.join(mainPath, row), filePath)
                with open(filePath, "r") as file:
                    dataJ["content"] = file.read()
                os.remove(filePath)
    return dataJ