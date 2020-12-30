import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = '5FYXQU6snSIAAAAAAAAAAaR9OOb-4qqnwZF2-ALsQo5UNqc1rQ7kmvdc6mb3z6fh'
    transferData = TransferData(access_token)

    file_from = input("Enter the path of file to be taken")
    file_to = input("Enter the path where the file is to be dropped")
    transferData.upload_file(file_from, file_to)
    print("Your file has been uploaded successfully")
    
main()