# bH5
A simple server side rendered platform which hosts your GPS Tracks. Simply paste gpx into the form and permalink or download geojson, gpx and an svg representation. In the django backend select if you want your tracks to be public. Browse the tracks via the user page or via search lat/long/radius for example. The tracks are stored in a postgresql database with postgis extension.

## run development environment
```
docker-compose up -d
```

## bugs
Don't use this. It's not stable. If you don't believe me have a look inside [bugs.md](./bugs.md)

## blauerHimmel
Translated into English blauer Himmel means blue sky. And blue sky is best for a good GPS fix. This is no my first attempt to. Back in 2012 a few friends and me we tried to build a tracking platform [blauerHimmel](https://github.com/koma5/blauerHimmel) with arduinos GPS receivers and a lot of brute force PHP without any frameworks. This is, mockingly attempt 5  hence the name *bH5*.
