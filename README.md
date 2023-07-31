# SankhyaResponseDeCrapIfier
Transforms the total crap Sankhya json response is into something nicer

For some reason the geniuses at [Sankhya](https://www.sankhya.com.br) decided that instead of modeling their json responses just like anyone else (you know, the normal way), they decided to make json act like xml, by sending first the name of all of the parameters names, and then sending the values, or what I like to call it **a totally unnecessary crap**.

If you wanna see how **crap** their response is, just look at [their documentation](https://developer.sankhya.com.br/reference/get_produto).

It's important to note that this only applies for `CRUDServiceProvider.loadRecords` responses, since other "methods" can return different kinds of crappy json content.


## usage

Usage should be pretty simple, just call the script informing the input file, like so:
```bash
python parser.py response.json
```
Alternatively, you can inform an output file, like so:
```bash
python parser.py response.json output.json
```

You can get a `response.json` file by saving it from Postman.

![image](https://github.com/kabessao/SankhyaResponseDeCrapIfier/assets/22626848/9ebfa0ee-c8ac-4a4e-94bf-99778a2ff2dd)


### Options

Some optional arguments we have are:
* `--filter-empty-values` will only list fields where values are not empty, be it `0` or `""`. Disabled by default;
* `--filter-customized-fields` will only list fields that are not part of customizations, those being fields starting with `AD_`. Disabled by default;

All of the cases above have negation versions by using `--no-` before it. (Ex.: `--no-filter-empty-values`).


# Before and After

Here is the crap json Sankhya sends:
```json
 {
    "serviceName": "CRUDServiceProvider.loadRecords",
    "status": "1",
    "pendingPrinting": "false",
    "transactionId": "7EC52EBA04CF6E5DB89BA44EE3C5A4CF",
    "responseBody": {
        "entities": {
            "total": "1",
            "hasMoreResult": "false",
            "offsetPage": "0",
            "offset": "0",
            "entity": {
                "f1": {
                    "$": "CANELA EM PO"
                },
                "f0": {
                    "$": "7"
                },
                "f3": {
                    "$": "UN"
                },
                "f2": {
                    "$": "JUNCO"
                },
                "f4": {
                    "$": "1000"
                }
            },
            "metadata": {
                "fields": {
                    "field": [
                        {
                            "name": "CODPROD"
                        },
                        {
                            "name": "DESCRPROD"
                        },
                        {
                            "name": "MARCA"
                        },
                        {
                            "name": "CODVOL"
                        },
                        {
                            "name": "CODLOCALPADRAO"
                        }
                    ]
                }
            }
        }
    }
}
```

and this is it "uncrapified":
```shell
[
    {
        "CODPROD": "7",
        "DESCRPROD": "CANELA EM PO",
        "MARCA": "JUNCO",
        "CODVOL": "UN",
        "CODLOCALPADRAO": "1000"
    }
]
```
