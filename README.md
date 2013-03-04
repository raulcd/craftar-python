# Catchoom Python Library


## Description

[Catchoom Recognition Service (CRS)](https://crs.catchoom.com/) is a web service
that allows you to build a wide range of __Image Recognition__ applications
and services.

This client library provides access to CRS APIs:
- [Catchoom Recognition API]
(http://support.catchoom.com/customer/portal/articles/796840-recognition-api)
  allows visual recognition against one of your _collections_ of reference
  _images_ specified using the collection _token_.
- [Catchoom Management API]
(http://support.catchoom.com/customer/portal/articles/982312-management-api)
  allows upload and management of _collections_ of reference _images_.
  All requests must be authenticated using your management api key.

The library also provides tools for performing batch operations:
- [catchoom_search](bin/catchoom_search), for image recognition.
- [catchoom_upload](bin/catchoom_upload), for batch upload of images.


## Installation

To install the library, simply run:

    pip install catchoom


## Dependencies

- [Requests](https://github.com/kennethreitz/requests)
- [Pillow](https://github.com/python-imaging/Pillow)


## Quick Start

Follow these steps to create a _collection_ with one _item_ and perform
a recognition against it. You can do it directly from your python interpreter.

1. Get [your management api_key](https://crs.catchoom.com/accounts/apis/).
This is needed for authenticating your requests to the management API.
    
    ```python
    import catchoom
    
    # use your own api_key!
    api_key = "35d5919334816e239bba08637e6aa457e8ca92c8"
    ```
    
2. Create a new _collection_.
  - A _collection_ is a set of _items_ representing entities that you want to
    recognize. Examples of _items_ are logos, physical objects, or a drawings,
    among others.
    
    ```python
    name = "My cool colection" # use your own collection name
    collection = catchoom.create_collection(api_key, name)
    ```

3. Keep the _token_ of that _collection_, you will need it later for
the recognition:

    ```python
    token_list = catchoom.get_token_list(api_key, limit=1, offset=0,
                                         collection=collection["uuid"])
    token = token_list[0]["token"] # first token on the list
    ```

4. Create an empty _item_ in your _collection_:

    ```python
    name = "My cool item" # use your own item name
    url = "http://catchoom.com" # and your own url
    custom = "This is my custom data" # and your own custom data
    item = catchoom.create_item(api_key, collection["uuid"], name, url, custom)
    ```

5. Upload an _image_ representing your _item_.
  - You can use one of the [reference images examples](images/reference).
  - Every _item_ can be represented by one or more reference _images_.
    This is useful for _items_ that have different faces, e.g. cereal boxes.
  - Before performing a successful recognition, the corresponding reference
    _image_ needs to be fully indexed by the server. Normally it takes
    less than one second after uploading.

    ```python
    filename = "catchy.png" # use your own image
    image = catchoom.create_image(api_key, item["uuid"], filename)
    ```

6. Now you are ready to perform the visual recognition against your collection.
  - You can use one of the [query images examples](images/query). You will also
    need the _token_ you saved in step 3 and the image to be recognized.

    ```python
    # remember that you set _token_ in step 3
    filename = "query_01.jpg" # use your own query image
    result_list = catchoom.search(token, filename)
    ```

7. Done! You can print the result:

    ```python
    print result_list
    ```
   - Each returned reference _image_ has an associated _score_,
     indicating its relevancy to the query image.


## Scripts

The scripts under [/bin](bin) allow batch operations against the APIs:
- [catchoom_search](bin/catchoom_search) sends one or several recognition
  requests against the Catchoom Recognition Service (CRS).
  Specifically, it performs visual scans against the _collection_
  (specified by the _token_) using every image in the provided directory.
- [catchoom_upload](bin/catchoom_upload) uploads a set of reference _images_
  to the Catchoom Recognition Service (CRS). It iterates over the contents of
  the specified directory and uploads all the images (and, if provided,
  also their associated metadata) to a new or an existing _collection_.


## Examples

In order to see reference implementations demonstrating the most common
operations that can be performed with these APIs check the scripts
under the [examples](examples) folder:
- [example_list_paginated_items](examples/example_list_paginated_items.py):
  Lists all your _items_. If required, the listed _items_ can be limited
  to a specific _collection_.
- [example_management](examples/example_management.py): Demonstrates listing,
  creation, updating and deletion of every type of object (i.e. _collection_,
  _item_, _image_, _token_).

For the reference implementation of the recognition operation see
the script [catchoom_search](bin/catchoom_search) script under [/bin](bin).

## Images

These are some images you can use in your tests:
- Images under [reference image](images/reference) can be uploaded
  to your collection.
- Images under [query images](images/query) can be used for performing
  visual recognition against your collection.


## Reporting Issues

If you have suggestions, bugs or other issues specific to this library, file
them [here](https://github.com/Catchoom/catchoom-python/issues) or contact us
at [support@catchoom.com](mailto:support@catchoom.com).
