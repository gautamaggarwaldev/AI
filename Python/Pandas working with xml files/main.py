import pandas as pd

xml = pd.read_xml("test.xml")

print(xml)

xml1 = '''<?xml version='1.0' encoding='utf-8'?>
<data xmlns="http://example.com">
 <row>
   <shape>square</shape>
   <degrees>360</degrees>
   <sides>4.0</sides>
   <firstname>GG</firstname>
 </row>
 <row>
   <shape>circle</shape>
   <degrees>360</degrees>
   <sides/>
   <firstname/>
 </row>
 <row>
   <shape>triangle</shape>
   <degrees>180</degrees>
   <sides>3.0</sides>
   <firstname/>
 </row>
</data>'''

print(pd.read_xml(xml1))


xml = '''<?xml version='1.0' encoding='utf-8'?>
<data>
  <row shape="square" degrees="360" sides="4.0" firstname="GG"/>
  <row shape="circle" degrees="360"/>
  <row shape="triangle" degrees="180" sides="3.0" lastname="AG"/>
</data>'''

print(pd.read_xml(xml,xpath=".//row"))

xml = '''<?xml version='1.0' encoding='utf-8'?>
<doc:data xmlns:doc="https://example.com">
  <doc:row>
    <doc:shape>square</doc:shape>
    <doc:degrees>360</doc:degrees>
    <doc:sides>4.0</doc:sides>
  </doc:row>
  <doc:row>
    <doc:shape>circle</doc:shape>
    <doc:degrees>360</doc:degrees>
    <doc:sides/>
  </doc:row>
  <doc:row>
    <doc:shape>triangle</doc:shape>
    <doc:degrees>180</doc:degrees>
    <doc:sides>3.0</doc:sides>
  </doc:row>
</doc:data>'''

df=pd.read_xml(xml,xpath=".//doc:row",namespaces={"doc": "https://example.com"})

print(df)

df.to_xml('test1.xml')