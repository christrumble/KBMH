Set objWord = CreateObject("Word.Application")
objWord.Visible = False

Dim objDoc
Set objDoc = objWord.Documents.Add()

Dim fso, inputFile, outputFile, strContent
Set fso = CreateObject("Scripting.FileSystemObject")

inputFile = objWord.ActiveDocument.Path & "\Order_Management_Follow-Up_Discovery_Session.md"
outputFile = objWord.ActiveDocument.Path & "\Order_Management_Follow-Up_Discovery_Session.docx"

On Error Resume Next
Set inFile = fso.OpenTextFile(inputFile, 1, False, -2)
strContent = inFile.ReadAll()
inFile.Close()
On Error GoTo 0

If strContent <> "" Then
    objDoc.Content.InsertAfter(strContent)
End If

objDoc.SaveAs(outputFile), 12

objDoc.Close(False)
objWord.Quit()
