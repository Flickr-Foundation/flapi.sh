# flapi.sh

This is a set of tiny command-line tools for experimenting with the [Flickr API].
It's very similar to the Flickr API Explorer, but in my terminal.

For example:

```console
$ flapi flickr.photos.getInfo photo_id=52782497889
<?xml version="1.0" encoding="utf-8"?>
<rsp stat="ok">
  <photo id="52782497889" secret="c92b337091" server="65535" farm="66" dateuploaded="1680219042" isfavorite="0" license="0" safety_level="0" rotation="0" views="5174" media="photo">
    …
```

I use these tools when I want to do some quick experiments with the API and get a particular value or see how some XML looks.

It's **not** meant for use in a production app – there are better ways to do that!

[Flickr API]: https://www.flickr.com/services/api/

## Usage

You can use the `flapi` script to call individual API methods.

You pass the method as one argument, and any query parameters as a second argument.
For example

```console
$ flapi flickr.photos.search user_id=124495553@N05&tag=radiotechnology
```

Some Flickr API methods don't need any query parameters, so you just pass the method:

```console
$ flapi flickr.commons.getInstitutions
```
