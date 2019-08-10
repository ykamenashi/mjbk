## mjbk: incomplete mojibake converter
### what is this?
* web-interface for mojibake, but incompletely.

### how to use(web interface)
#### endpoint
> http://localhost:80/cgi-bin/index.cgi?key=value

#### example
> http://localhost:80/cgi-bin/?a=隣の客はよく柿食う客だ

#### response
```json
{
  "key": "a",
  "value": "隁vぃ�宁uぃbよく柃\食う宁u�"
}
```

### based on
* [nkf](https://ja.osdn.net/projects/nkf/)