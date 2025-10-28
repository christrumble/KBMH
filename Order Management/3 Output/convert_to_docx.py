import subprocess
import os

md_file = r'Order_Management_Follow-Up_Discovery_Session.md'
docx_file = r'Order_Management_Follow-Up_Discovery_Session.docx'

# Read the markdown file
with open(md_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Use cmd to create a docx from markdown via Word
vbs_script = '''
Set objWord = CreateObject("Word.Application")
objWord.Visible = False

Set objDoc = objWord.Documents.Add()

' Get the markdown content
strContent = "CONTENT_PLACEHOLDER"

' Add content
objDoc.Content.InsertAfter(strContent)

' Save as docx
strPath = "FILEPATH_PLACEHOLDER"
objDoc.SaveAs(strPath), 12

objDoc.Close()
objWord.Quit()
'''

vbs_script = vbs_script.replace('CONTENT_PLACEHOLDER', content.replace('"', '\\"'))
vbs_script = vbs_script.replace('FILEPATH_PLACEHOLDER', os.path.abspath(docx_file))

with open('temp_convert.vbs', 'w') as f:
    f.write(vbs_script)

subprocess.run(['cscript.exe', 'temp_convert.vbs'])
print("Document created: " + docx_file)
