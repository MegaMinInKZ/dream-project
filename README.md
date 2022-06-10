# DREAM PROJECT
# API endpoints for Easy Way application
## Authenticating requests
This API is not authenticated.
## Endpoints
### Display all the cities
[GET] 127.0.0.1:8000/api/v1/cityList
![city-list](https://user-images.githubusercontent.com/90828152/173030512-dd0d6c67-ee95-405c-9ba3-60c434736233.png)
### Display all the shops
[GET] 127.0.0.1:8000/api/v1/shopList
![shop-list](https://user-images.githubusercontent.com/90828152/173030571-39a19c35-cfc7-463a-9cf4-57e52b1ded93.png)
### Display all the categories
[GET] 127.0.0.1:8000/api/v1/categoryList
![category-List](https://user-images.githubusercontent.com/90828152/173030604-4687cc80-0b4e-4450-ada4-82602b5eea3a.png)
### Display all products in the specified category
[GET] 127.0.0.1:8000/api/v1/category/{category slug}/
![category1](https://user-images.githubusercontent.com/90828152/173030715-f21a1387-f261-4b8f-b246-55da926def18.png)
![category2](https://user-images.githubusercontent.com/90828152/173030737-12ba9358-99b0-43ff-aa01-ff429aabf93f.png)
### Display all products in the specified city
[GET] 127.0.0.1:8000/api/v1/city/{city slug}/
![city1](https://user-images.githubusercontent.com/90828152/173030787-805e118c-12b5-4aa4-ad90-6d1ff951f3af.png)
![city2](https://user-images.githubusercontent.com/90828152/173030806-e87cdc75-8104-4897-9532-65ee03488a0a.png)
### Display all products in the specified shop
[GET] 127.0.0.1:8000/api/v1/shop/{shop slug}/
![shop1](https://user-images.githubusercontent.com/90828152/173030835-cadee84a-c3cf-4db6-af21-349c1387cb9c.png)
![shop2](https://user-images.githubusercontent.com/90828152/173030857-f9bde851-c72c-4536-9bc5-5364c53e77d1.png)
### Display all information about specified product
[GET] 127.0.0.1:8000/api/v1/product/{product slug}/
![product-info](https://user-images.githubusercontent.com/90828152/173031127-48cc8b52-0f9f-4687-a4f6-e762457cb1d7.png)
