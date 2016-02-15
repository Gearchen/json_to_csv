#Json2Csv

Convert json into csv format

Written in Python 2.7.11

##Usage
<pre><code>python json2csv.py file_in_json_format_to_transform</code></pre>

##Example
<pre><code>[
{
	"id":1,
	"name_cn":"name_1",
	"name_en":"name_1",
	"parentId":0
},
{
	"id":2,
	"name_cn":"name_2",
	"name_en":"name_2",
	"parentId":2
},
{
	"id":3,
	"name_cn":"name_3",
	"name_en":"name_3",
	"parentId":6
}
]</code></pre>

Output:
<pre><code>id,name_cn,name_en,parentId
1,name_1,name_1,0
2,name_2,name_2,2
3,name_3,name_3,6
</code></pre>

##Notice

* not suitable for nested json file
* write two files to present path, json & csv


