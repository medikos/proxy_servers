# proxy_servers
Creating a list of proxy servers
___
Example

```python
   from ProxyO import ProxyCreator
   creator = ProxyO()
   creator.list_proxy() # simple list of proxy servers 
   creator.list_proxy(country='ru') # list of proxy servers filtered by country
   creator.list_proxy(port=80) # list of proxy servers filtered by port
```
