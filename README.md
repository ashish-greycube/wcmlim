### Wcmlim

Customization for Woocommerce Multilocations Invnetory Management

WooCommerce Admin Task
======================
[1] purchase and install 
https://codecanyon.net/item/woocommerce-multi-locations-inventory-management/28949586

[2] install  to enable legacy REST API
https://wordpress.org/plugins/woocommerce-legacy-rest-api/
<img width="1305" height="581" alt="image" src="https://github.com/user-attachments/assets/0738c6cd-478d-4738-9c0d-aaee45810c84" />

[3] update key 
https://test.daralzbrj.com.sa/wp-admin/edit-tags.php?page=multi-location-inventory-management
<img width="1439" height="850" alt="image" src="https://github.com/user-attachments/assets/c96278a9-5aeb-4687-9d4b-518af3c3e5d5" />


[4] Enable Rest API
https://test.daralzbrj.com.sa/wp-admin/admin.php?page=wc-settings&tab=advanced&section=keys
https://test.daralzbrj.com.sa/wp-admin/admin.php?page=wc-settings&tab=advanced&section=keys&edit-key=1
<img width="1453" height="641" alt="image" src="https://github.com/user-attachments/assets/79119c96-8944-45bd-9f26-abbe96292046" />



Task in ERPNext
==============

[1]Enable Stock Level Synchronisation and put all warehouse
https://testdarco15.etqansoft.com/app/woocommerce-server/test.daralzbrj.com.sa
<img width="1180" height="850" alt="image" src="https://github.com/user-attachments/assets/3e7b5f9e-cb85-4aad-9791-42ac73cce47f" />


[2] Update SO : Fields Mapping
https://testdarco15.etqansoft.com/app/woocommerce-server/test.daralzbrj.com.sa
"custom_wcmlim_location_id | wcmlim_location_id" $.meta_data[?(@.key=='_selectedLocTermId')].value
<img width="1368" height="1017" alt="image" src="https://github.com/user-attachments/assets/2ffa3e5f-615c-4484-98ea-bd6044a10043" />


[3] fetch location mapping
https://testdarco15.etqansoft.com/app/wcmlim-settings
<img width="1446" height="673" alt="image" src="https://github.com/user-attachments/assets/81c98334-d1c6-4a3f-bf1a-26728397a600" />


### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app wcmlim
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/wcmlim
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
