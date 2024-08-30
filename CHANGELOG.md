# CHANGELOG

## 2024-06-05

*   Allow looking up users with `fluser` from a URL to one of their photos.
    For example:

    ```console
    $ fluser https://www.flickr.com/photos/197130754@N07/53630778857/
    $ fluser https://www.flickr.com/photos/flickrfoundation/53630778857/
    ```

*   Add some tests for the scripts; run the tests in GitHub Actions.

## 2024-04-11

*   Initial version of `flapi`; call Flickr API methods with optional parameters.
    For example:

    ```console
    $ flapi flickr.commons.getInstitutions
    $ flapi flickr.profile.getProfile user_id=197130754@N07"
    ```

*   Initial version of `flphoto`; look up photos with their photo ID, or a URL to the photo.
    For example:

    ```console
    $ flphoto 53630778857
    $ flphoto https://www.flickr.com/photos/flickrfoundation/53630778857/
    ```

*   Initial version of `fluser`; look up users with their Flickr NSID, a URL to their profile on Flickr.com, or a URL to their profile on <https://commons.flickr.org>.
    For example:

    ```console
    $ fluser 197130754@N07
    $ fluser https://www.flickr.com/people/197130754@N07
    $ fluser https://www.flickr.com/photos/flickrfoundation/
    ```
