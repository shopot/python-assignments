# Assignment: Python basics

Task name: `Python basics`

Repository name: `python-basics`

## Description

Your task is to complete several simple tasks to learn Python basics.

Creating a new repository on GitHub named `python-basics`.

Clone `python-basics` branch from this repository:

```shell
git clone -b python-basics https://github.com/shopot/python-assignments.git --single-branch
mv python-assignments python-basics
cd python-basics
rm -rf .git
git init
git remote add origin https://github.com/<username>/python-basics.git
git add .
git commit -a -m "init: start project"
git branch -M main
git push -u origin main
```

Assignment contains several nested folders inside `src`. Your task is to implement necessary functionality inside them.

### Technical requirements

- Any external tools and libraries are prohibited
- Use Python 3.11 version
- Don't change signature of pre-written functions (e.g. don't rename them, etc.)
- Prefer Asynchronous I/O whenever possible

### Subtasks list

1. File system (src/fs)
2. Command line interface (src/cli)
3. Hash (src/hash)
4. Streams (src/streams)
5. Zlib (src/zip)
6. Worker Threads (src/wt)
7. Child Processes (src/cp)

## Subtasks description

### 1. File system (src/fs)

You should implement several functions in dedicated files

- `create.py` - implement function that creates new file `fresh.txt` with content `I am fresh and young` inside of the `files` folder (if file already exists `Error` with message `FS operation failed` must be thrown)
- `copy.py` - implement function that copies folder `files` files with all its content into folder `files_copy` at the same level (if `files` folder doesn't exists or `files_copy` has already been created `Error` with message `FS operation failed` must be thrown)
- `rename.py` - implement function that renames file `wrongFilename.txt` to `properFilename` with extension `.md` (if there's no file `wrongFilename.txt` or `properFilename.md` already exists `Error` with message `FS operation failed` must be thrown)
- `delete.py` - implement function that deletes file `fileToRemove.txt` (if there's no file `fileToRemove.txt` `Error` with message `FS operation failed` must be thrown)
- `list.py` - implement function that prints all array of filenames from `files` folder into console (if `files` folder doesn't exists `Error` with message `FS operation failed` must be thrown)
- `read.py` - implement function that prints content of the `fileToRead.txt` into console (if there's no file `fileToRead.txt` `Error` with message `FS operation failed` must be thrown)

### 2. Command line interface (src/cli)

You should implement several functions in dedicated files

- `env.py` - implement function that parses environment variables with prefix `PY_` and prints them to the console in the format `PY_name1=value1; PY_name2=value2`
- `args.py` - implement function that parses command line arguments (given in format `--propName value --prop2Name value2`, you don't need to validate it) and prints them to the console in the format `propName is value, prop2Name is value2`

### 3. Hash (src/hash)

You should implement several functions in dedicated files

- `calc_hash.py` - implement function that calculates SHA256 hash for file `fileToCalculateHashFor.txt` and logs it into console as `hex` using Streams API

### 4. Streams (src/streams)

You should implement several functions in dedicated files

- `read.py` - implement function that reads file `fileToRead.txt` content using Readable Stream and prints it's content into `sys.stdout`
- `write.py` - implement function that writes `sys.stdin` data into file `fileToWrite.txt` content using Writable Stream
- `transform.py` - implement function that reads data from `sys.stdin`, reverses text using streams transforms and then writes it into `sys.stdout`

### 5. Zlib (src/zip)

You should implement several functions in dedicated files

- `compress.py` - implement function that compresses file `fileToCompress.txt` to `archive.gz` using `zlib` and async stream
- `decompress.py` - implement function that decompresses `archive.gz` back to the `fileToCompress.txt` with same content as before compression using `zlib` and async stream

### 7. Worker Threads (src/wt)

You should implement several functions in dedicated files

- `worker.py` - extend given function to work with data received from main thread and implement function which sends result of the computation to the main thread
- `main.py` - implement function that creates number of worker threads (equal to the number of host machine logical CPU cores) from file `worker.py` and able to send data to those threads and to receive result of the computation from them. You should send incremental number starting from `10` to each `worker`. For example: on host machine with **4** cores you should create **4** workers and send **10** to first `worker`, **11** to second `worker`, **12** to third `worker`, **13** to fourth `worker`. After all workers will finish, function should log array of results into console. The results are array of objects with 2 properties:
  - `status` - `'resolved'` in case of successfully received value from `worker` or `'error'` in case of error in `worker`
  - `data` - value from `worker` in case of success or `null` in case of error in worker.

The results in the array must be in the same order that the workers were created.

### 8. Child Processes (src/cp)

You should implement several functions in dedicated files

- `cp.py` - implement function `spawn_child_process` that receives array of arguments `args` and creates child process from file `child.py`, passing these `args` to it. This function should use a Queue to pass messages back and forth.

```

```
