### Wcmlim

Customization for Woocommerce Multilocations Invnetory Management

WooCommerce Admin Task
======================
[1] purchase and install 
https://codecanyon.net/item/woocommerce-multi-locations-inventory-management/28949586

[2] install  to enable legacy REST API
https://wordpress.org/plugins/woocommerce-legacy-rest-api/
success_phot

[3] update key 
https://test.daralzbrj.com.sa/wp-admin/edit-tags.php?page=multi-location-inventory-management
success_phot

[4] Enable Rest API
https://test.daralzbrj.com.sa/wp-admin/admin.php?page=wc-settings&tab=advanced&section=keys
https://test.daralzbrj.com.sa/wp-admin/admin.php?page=wc-settings&tab=advanced&section=keys&edit-key=1
success_phot


Task in ERPNext
==============

[1]Enable Stock Level Synchronisation and put all warehouse
https://testdarco15.etqansoft.com/app/woocommerce-server/test.daralzbrj.com.sa
success_phot

[2] Update SO : Fields Mapping
https://testdarco15.etqansoft.com/app/woocommerce-server/test.daralzbrj.com.sa
"custom_wcmlim_location_id | wcmlim_location_id" $.meta_data[?(@.key=='_selectedLocTermId')].value
success_phot

[3] fetch location mapping
https://testdarco15.etqansoft.com/app/wcmlim-settings
success_phot

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
