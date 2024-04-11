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

### flapi - call the API

You can use the `flapi` script to call individual API methods.
It pretty-prints the XML returned from the API, with syntax highlighting.

You pass the method as one argument, and any query parameters as a second argument.
For example:

```console
$ flapi flickr.photos.search user_id=124495553@N05&tag=radiotechnology
```

Some Flickr API methods don't need any query parameters, so you just pass the method:

```console
$ flapi flickr.commons.getInstitutions
```

The nice thing about `flapi` is that I can wrap it to build other small tools for digging into the API.

### flphoto - get a single photo

You can use the `flphoto` script to get information about a single photo, using the [flickr.photos.getInfo API](https://www.flickr.com/services/api/flickr.photos.getInfo.html).

You pass the photo ID or a URL to the photo as a single argument.
For example:

```console
$ flphoto 52783721105
$ flphoto https://www.flickr.com/photos/nypl/4058778064/
```

### fluser - look up a user

You can use the `fluser` script to get information about a single user.

You can pass their NSID, or a URL to their profile page on Flickr, for example:

```console
$ fluser "https://www.flickr.com/photos/12403504@N02/"
NSID:     12403504@N02
username: The British Library
realname: British Library
URL:      https://www.flickr.com/photos/britishlibrary
```

I find this particularly useful when I need to quickly look up the NSID for a user whose profile I'm looking at.

## Installation

You need the following tools for `flapi`:

*   [curl](https://curl.se/), to make HTTP requests
*   [keyring](https://github.com/jaraco/keyring), to get a Flickr API key from your system keychain
*   [Pygments](https://pygments.org/), for syntax highlighting
*   xmllint, for pretty-printing XML

You need additional tools for `flphoto` and `fluser`:

*   [flickr-url-parser](https://pypi.org/project/flickr-url-parser/), to parse Flickr URLs
*   [jq](https://jqlang.github.io/jq/), to parse JSON

Once you have all your tools installed, get yourself a [Flickr API key](https://www.flickr.com/services/api/) and save it in your system keychain:

```console
$ keyring set flickr_api key
Password for 'key' in 'flickr_api': <Enter your API key here>
```

Then add this repo to your PATH, and you can run the scripts.

## License

MIT.
