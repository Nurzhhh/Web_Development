import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductAlertsComponent } from './product-alerts/product-alerts.component';
import { ProductDetailsComponent } from './product-details/product-details.component';
// import { CartService } from './test2.service';
// import { CartComponent } from './test2/test2.component';
import { HttpClientModule } from '@angular/common/http';
// import { ShippingComponent } from './test1/test1.component';
import { ProductItemComponent } from './product-item/product-item.component';

@NgModule({
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      { path: '', component: ProductListComponent  },
      { path: 'categories/:categoriesId', component: ProductItemComponent },
      { path: 'products/:productsIdpro', component: ProductDetailsComponent },
      // { path: 'test2', component: CartComponent },
      // { path: 'test1', component: ShippingComponent },
    ])
  ],
  declarations: [
    AppComponent,
    TopBarComponent,
    ProductListComponent,
    ProductAlertsComponent,
    ProductDetailsComponent,
    // CartComponent,
    // ShippingComponent,
    ProductItemComponent
  ],
  bootstrap: [
    AppComponent
  ],
  // providers: [CartService]
})
export class AppModule { }
