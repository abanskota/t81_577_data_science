## Learning objective: Learn how to open and read generic text files in python

In the previous sections, we learnt how to ingest data into python from PostgreSQL and REST APIS. While data is mainly served through databases and APIs in industry settings these days, very often we still need to read data from variously formatted files. Python handles two generic types of files: binary and text files. 

Popular libraries for data science like Pandas have inbuilt methods to read various types of text and binary  files and even reading data from databases. We will learn some of the techniques next week in detail. There are also libraries such as `csv` , `openpyxl` , and `PIL` to read specific file formats. In this lesson, we will focus on learning to use builtin python functions like `open` and `read` to open a text file and read contents into Python. 

### Opening and closing a text file in python


The first thing we do while importing data from a file is to open it. The built-in function `open()` is used for that purpose. 
The open function has two commonly used arguments, 
- Filepath (required)
- Access Mode (optional)

For example, the following command will open the CSV file located in `files` folder in week5 folder:

```python
CSV_FILE = “/home/asimbanskota/t81_577_data_science/weekly_materials/week5/files/city.csv”
file = open(CSV_FILEPATH, ‘r’)
```
The second argument 'r' is an argument for access mode that tells Python to open the file for read only mode, which is also a default mode. The open method returns a file object called "handle". 

It is the best-practice to close a file properly when the purpose of opening the file is fulfilled. It can be done by calling the close method on the file handle object using a try-finally block as follows: 

```python
try:
    file = open(CSV_FILE, ‘r’)
    # do something with it
finally:
    file.close()
```

Even better, `with` statement can be used t do the same without the need for remembering to close the file.

```python
with open (CSV_FILE, "r") as file:
    # Do something with it
```

### Reading opened files

Once opened, we can read the file contents using one of the following three file objects.

1. `.read(size = -1)` 
<ul>

- Reads the file content matching the `size` bytes; if no argument or negative 1 is passed, then the entire file is read.

```python
with open (CSV_FILE, "r") as file:
    file.read(30)
```
Which outputs 29 characters going into the second line plus one related to newline character:
```shell
id,lat,lon,city,state
0,41,80,
```
</ul>


2. `.readline(size =-1)`

<ul>
    
- Reads one entire line from the file with negative 1 or no argument. Otherwise, it will read the number of characters in a line not exceeding the size byte.
    
```python
with open (CSV_FILE, "r") as file:
    file.readline(30)
```
Which outputs the entire first line:
    
```shell
id,lat,lon,city,state
```
    
We can iterate over each single line of the file:
  
```python
with open (CSV_FILE, "r") as file:
    for line in range(5):
        print(file.readline())
```

The above code outputs 5 lines as follows:

    ```shell
    id,lat,lon,city,state
    ```

0,41,80," ""Youngstown""", OH

1,42,97," ""Yankton""", SD

2,46,120," ""Yakima""", WA

3,42,71," ""Worcester""", MA
    ```
 </ul>
 
 
3. `.readlines()`: 

<ul>

- Reads all lines until the end of file is encountered and return the lines in a list.

```python
with open (CSV_FILE, "r") as file:
    file.readlines()
```
</ul>

Though we only went through opening a csv file here, all the above discussed methods work similarly with all different types of text files.


