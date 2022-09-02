# HTTPS
https://github.com/Yuwu12292/shiyan.git
## Highlights
* Super easy to use, no source code change for most features
* Use yaml files to record arbitrary functions/variables without changing the code
* Available for Linux/MacOS/Windows

## Install

The preferred method for installing dependent packages is via apt or pip

```sh
pip install 
apt update
apt search opencv
```

## Basic Usage

### Command Line

Assume you have a python script to run , you can first look at its optional parameters:

```sh
python3.8 my_script.py -h
```

You can simply use stream_filter by

```
./stream_filter video_name.mp4
```

<details>
<summary>
 A <code>folder</code> with the name of the video name containing <code>the extracted pictures </code>will be generated
</summary>
</details>

### Inline

You can also manually set breakpoints in your script for code debugging.

```python
import pdb

pdb.set_trace

```


## Advanced Usage

### No need to change the code of the yaml file

Editordata.yaml supports implementing various functions without changing the source code .
Be sure to read carefully and use its internal instructions to implement each feature

### Add Custom Event

* [Instant Event](https://viztracer.readthedocs.io/en/stable/custom_event_intro.html#instant-event)
* [Variable Event](https://viztracer.readthedocs.io/en/stable/custom_event_intro.html#variable-event)
* [Duration Event](https://viztracer.readthedocs.io/en/stable/custom_event_intro.html#duration-event)



## Documentation

For full documentation, please see [https://github.com/Yuwu12292/shiyan/blob/main/README.md](https://github.com/Yuwu12292/shiyan/blob/main/README.md)

## Bugs/Requests

Please send bug reports and feature requests through [github issue tracker](https://github.com/gaogaotiantian/viztracer/issues). Shiyan is currently under development now and it's open to any constructive suggestions.

## License

Copyright Yu Wu, 2022.

Distributed under the terms of the  [Apache 2.0 license](https://github.com/gaogaotiantian/viztracer/blob/master/LICENSE).
