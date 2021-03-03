import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { products } from '../products';
import { categories } from '../categories';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {

  products = products;
  categories = categories;
  product;
  category;
  categoryIdd;

  share(link,description) {
    let ur = "https://t.me/share/url?url=" + link + "&text" + description;
    window.open(ur, "_blank");
  }

  constructor(
    private route: ActivatedRoute
  ) {}
  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }
  ngOnInit() {
    const routeParams = this.route.snapshot.paramMap;
    const categoryIdFromRoute = Number(routeParams.get('categoriesId'));
    this.categoryIdd = categoryIdFromRoute;
    this.product = products.find(product => product.id === categoryIdFromRoute);
    this.category = products.find(category => category.id === categoryIdFromRoute);
  }
  likeItem(idpro) {
    products[idpro].likes += 1
  }
  removeItem(idpro) {
    products.splice(idpro, 1)
    for (var i = idpro; i< products.length; i++) {
      products[i].idpro = i
    }
  }
}
