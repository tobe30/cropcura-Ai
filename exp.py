# # @login_required
# # def index(request):
# #     # Total stats
# #     # Average cost per unit from all purchases
# #     total_revenue = Sale.objects.aggregate(
# #     total=Sum(F('unit_sold') * F('price'), output_field=FloatField())
# #     )['total'] or 0
    
# #     total_inventory_value = sum(
# #     (p.current_stock or 0) * p.average_cost() for p in Product.objects.all()
# # )



# # # Now, actual gross profit:
    
# #     total_cost = Purchase.objects.aggregate(
# #          total=Sum(F('unit_purchased') * F('price'), output_field=FloatField())
# #     )['total'] or 0


# #     total_units_bought = Purchase.objects.aggregate(total=Sum('unit_purchased'))['total'] or 0
# #     total_units_sold = Sale.objects.aggregate(total=Sum('unit_sold'))['total'] or 0
# #     low_stock_count = Product.objects.filter(current_stock__lt=10).count()
# #     total_products = Product.objects.count()
# #     recent_products = Product.objects.all().order_by('-id')[:4]

# #     # Per-product breakdown
# #     product_data = []
# #     products = Product.objects.all()
# #     for product in products:
# #         sales = Sale.objects.filter(product=product).aggregate(
# #             units_sold=Coalesce(Sum('unit_sold', output_field=FloatField()), V(0), output_field=FloatField()),
# #             revenue=Coalesce(Sum(F('unit_sold') * F('price'), output_field=FloatField()), V(0), output_field=FloatField()),
# #         )

# #         purchases = Purchase.objects.filter(product=product).aggregate(
# #             total_cost=Coalesce(Sum(F('unit_purchased') * F('price'), output_field=FloatField()), V(0), output_field=FloatField()),
# #             total_units=Coalesce(Sum('unit_purchased'), V(0))
# #         )
# #         average_cost = (
# #             purchases['total_cost'] / purchases['total_units']
# #             if purchases['total_units'] else 0
# #     )
        
# #         cost_for_units_sold = sales['units_sold'] * average_cost
# #         profit = sales['revenue'] - cost_for_units_sold

# #         stock = product.current_stock or 0  # if None, treat as 0

# #         if stock == 0:
# #             stock_status = "Out of Stock"
# #         elif stock < 10:
# #             stock_status = "Low Stock"
# #         else:
# #             stock_status = "Available"




# #         product_data.append({
# #             'product': product.name,
# #             'units_bought': purchases['total_units'],
# #             'units_sold': sales['units_sold'],
# #             'revenue': round(sales['revenue'], 2),
# #             'cost': round(cost_for_units_sold, 2),
# #             'profit': round(profit, 2),
# #             'stock_status': stock_status,
# #     })

# #     # 📊 Monthly sales vs purchase chart
# #     current_year = now().year

# #     sales_by_month = (
# #          Sale.objects
# #          .filter(sales_date__year=current_year)
# #          .annotate(month=TruncMonth('sales_date'))
# #          .values('month')
# #          .annotate(
# #           total_sales=Coalesce(
# #             Sum(F('unit_sold') * F('price'), output_field=FloatField()),
# #             V(0),
# #             output_field=FloatField()
# #         )
# #     )
# #     .order_by('month')
# # )


# #     purchases_by_month = (
# #       Purchase.objects
# #       .filter(purchase_date__year=current_year)
# #       .annotate(month=TruncMonth('purchase_date'))
# #       .values('month')
# #       .annotate(
# #         total_purchase=Coalesce(
# #             Sum(F('unit_purchased') * F('price'), output_field=FloatField()),
# #             V(0),
# #             output_field=FloatField()
# #         )
# #     )
# #     .order_by('month')
# # )


# #     monthly_data = {}
# #     for i in range(1, 13):
# #         month_name = calendar.month_abbr[i]
# #         monthly_data[month_name] = {'sales': 0, 'purchase': 0}

# #     for entry in sales_by_month:
# #         month = calendar.month_abbr[entry['month'].month]
# #         monthly_data[month]['sales'] = round(entry['total_sales'], 2)

# #     for entry in purchases_by_month:
# #         month = calendar.month_abbr[entry['month'].month]
# #         monthly_data[month]['purchase'] = round(entry['total_purchase'], 2)

# #     # Prepare chart lists
# #     labels = list(monthly_data.keys())
# #     sales = [monthly_data[m]['sales'] for m in labels]
# #     purchases = [monthly_data[m]['purchase'] for m in labels]
# #     profits = [s - p for s, p in zip(sales, purchases)]

# #     # Final context
# #     context = {
# #         'total_revenue': round(total_revenue, 2),
# #         'total_cost': round(total_cost, 2),
# #         'profit': total_inventory_value,
# #         'total_units_bought': total_units_bought,
# #         'total_units_sold': total_units_sold,
# #         'low_stock_count': low_stock_count,
# #         'total_products': total_products,
# #         'recent_products': recent_products,
# #         'product_data': product_data,
# #         'labels': labels,
# #         'sales_data': sales,
# #         'purchase_data': purchases,
# #         'profit_data': profits,
# #     }

# #     return render(request, 'dashboard/index.html', context)





# {% extends 'includes/base.html' %}
# {% load static %}
# {% block content%}
# {% load humanize %}

# <div class="page-wrapper">
# <div class="content">
# <div class="row">
# <div class="col-lg-3 col-sm-6 col-12">
# <div class="dash-widget">
# <div class="dash-widgetimg">
# <span><img src="{% static 'assets/img/icons/dash2.svg' %}" alt="img"></span>
# </div>
# <div class="dash-widgetcontent">
# <h5>€<span class="counters">{{ total_revenue }}</span></h5>
# <h6>Total Revenue</h6>
# </div>
# </div>
# </div>
# <div class="col-lg-3 col-sm-6 col-12">
# <div class="dash-widget dash1">
# <div class="dash-widgetimg">
# <span><img src="{% static 'assets/img/icons/dash1.svg' %}" alt="img"></span>
# </div>
# <div class="dash-widgetcontent">
# <h5>€<span class="counters">{{ total_cost }}</span></h5>
# <h6>Total Cost</h6>
# </div>
# </div>
# </div>
# <div class="col-lg-3 col-sm-6 col-12">
# <div class="dash-widget dash2">
# <div class="dash-widgetimg">
# <span><img src="{% static 'assets/img/icons/dash2.svg' %}" alt="img"></span>
# </div>
# <div class="dash-widgetcontent">
# <h5>€<span class="counters">{{ profit }}</span></h5>
# <h6>Inventory Value</h6>
# </div>
# </div>
# </div>
# <div class="col-lg-3 col-sm-6 col-12">
# <div class="dash-widget dash3">
# <div class="dash-widgetimg">
# <span><img src="{% static 'assets/img/icons/dash4.svg' %}" alt="img"></span>
# </div>
# <div class="dash-widgetcontent">
# {% for profit_data in product_data%}
# {% if profit_data.profit > 0 %}
# <h5 style="color: green;"><span class="counters" >Your Gaining</span></h5>
# {% elif profit_data.profit < 0 %}
# <h5 style="color: red;"><span class="counters" >your at loss</span></h5>
#  {% else %}
#  <h5 style="color: orange;"><span class="counters" >Breakeven</span></h5>
#   {% endif %}
#   {%empty%}
#   <h5><span class="counters" >No Data Yet</span></h5>
#   {% endfor %}
# </div>
# </div>
# </div>
# <div class="col-lg-3 col-sm-6 col-12 d-flex">
# <div class="dash-count">
# <div class="dash-counts">
# <h4>{{ total_units_bought }}</h4>
# <h5>Total Units Bought </h5>
# </div>
# <div class="dash-imgs">
# <i data-feather="user"></i>
# </div>
# </div>
# </div>
# <div class="col-lg-3 col-sm-6 col-12 d-flex">
# <div class="dash-count das1">
# <div class="dash-counts">
# <h4>{{ total_units_sold }}</h4>
# <h5>Total Units Sold</h5>
# </div>
# <div class="dash-imgs">
# <i data-feather="user-check"></i>
# </div>
# </div>
# </div>
# <div class="col-lg-3 col-sm-6 col-12 d-flex">
# <div class="dash-count das2">
# <div class="dash-counts">
# <h4>{{ low_stock_count }}</h4>
# <h5>Low Stock Items </h5>
# </div>
# <div class="dash-imgs">
# <i data-feather="file-text"></i>
# </div>
# </div>
# </div>
# <div class="col-lg-3 col-sm-6 col-12 d-flex">
# <div class="dash-count das3">
# <div class="dash-counts">
# <h4>{{ total_products }}</h4>
# <h5>Total Products </h5>
# </div>
# <div class="dash-imgs">
# <i data-feather="file"></i>
# </div>
# </div>
# </div>
# </div>

# <div class="row">
# <div class="col-lg-7 col-sm-12 col-12 d-flex">
# <div class="card flex-fill">
# <div class="card-header pb-0 d-flex justify-content-between align-items-center">
# <h5 class="card-title mb-0">Purchase Vs Sales</h5>
# <div class="graph-sets">
# <ul>
# <li>
# <span>Sales</span>
# </li>
# <li>
# <span>Purchase</span>
# </li>
# </ul>
# </div>
# </div>
# <div class="card-body">
#     <canvas id="salesChart" height="200"></canvas>
#   </div>
# </div>
# </div>
# <div class="col-lg-5 col-sm-12 col-12 d-flex">
# <div class="card flex-fill">
# <div class="card-header pb-0 d-flex justify-content-between align-items-center">
# <h4 class="card-title mb-0">Recently Added Products</h4>
# <div class="dropdown">
# <a href="javascript:void(0);" data-bs-toggle="dropdown" aria-expanded="false" class="dropset">
# <i class="fa fa-ellipsis-v"></i>
# </a>
# <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
# <li>
# <a href="{% url 'dashboard:productlist' %}" class="dropdown-item">Product List</a>
# </li>
# <li>
# <a href="{% url 'dashboard:addproduct' %}" class="dropdown-item">Product Add</a>
# </li>
# </ul>
# </div>
# </div>
# <div class="card-body">
# <div class="table-responsive dataview">
# <table class="table datatable ">
# <thead>
# <tr>
# <th>Sno</th>
# <th>Products</th>
# <th>Cost per Unit</th>
# </tr>
# </thead>
# <tbody>
# {% for p in recent_products %}
# <tr>
# <td>{{p.item_id}}</td>
# <td class="productimgname">
# <a href="{% url 'dashboard:productlist' %}" class="product-img">
    
# </a>
# <a href="{% url 'dashboard:productlist' %}">{{ p.name }}</a>
# </td>
# <td>€{{ p.average_cost|floatformat:2|intcomma }}</td>
# </tr>
# {% empty %}
# <p style="color: red;">Nothing to show</p>
# {% endfor %}
# </tbody>
# </table>
# </div>
# </div>
# </div>
# </div>
# </div>
# <div class="card mb-0">
# <div class="card-body">
# <h4 class="card-title">Profit per product Tracking</h4>
# <div class="table-responsive dataview">
# <table class="table datatable ">
# <thead>
# <tr>
# <th>Product</th>
# <th>Units Bought</th>
# <th>Unit Sold</th>
# <th>Total Revenue</th>
# <th>Total Cost</th>
# <th>Profit</th>
# <th>Status</th>
# </tr>
# </thead>
# <tbody>
#   {% for item in product_data %}
#     <tr>
#       <td>{{ item.product }}</td>
#       <td>{{ item.units_bought }}</td>
#       <td>{{ item.units_sold }}</td>
#       <td>€{{ item.revenue|floatformat:2|intcomma }}</td>
#       <td>€{{ item.cost|floatformat:2|intcomma }}</td>
#       <td>
#         {% if item.profit < 0 %}
#           <span class="text-danger">-€{{ item.profit|floatformat:2|intcomma }}</span>
#         {% else %}
#           <span class="text-success">€{{ item.profit|floatformat:2|intcomma }}</span>
#         {% endif %}
#       </td>
#       <td>
#         {% if item.stock_status == "Out of Stock" %}
#           <span class="badge bg-danger">{{ item.stock_status }}</span>
#         {% elif item.stock_status == "Low Stock" %}
#           <span class="badge bg-warning text-dark">{{ item.stock_status }}</span>
#         {% else %}
#           <span class="badge bg-success">{{ item.stock_status }}</span>
#         {% endif %}
#       </td>
#     </tr>
#   {% empty %}
   
#       <p colspan="7" class="text-center text-danger">No Product Data Available</p>
  
#   {% endfor %}
# </tbody>

# </table>
# </div>
# </div>
# </div>
# </div>
# </div>
# </div>

# {% endblock content %}


# # Extra dashboard stats
# total_units_sold = bc_products.aggregate(total=Sum('total_sold'))['total'] or 0
# low_stock_count = BC.objects.filter(current_stock__lt=5).count()
# total_products = (
#     Product.objects.count() +
#     BC.objects.count() +
#     Number8.objects.count() +
#     Ds9c.objects.count() +
#     Np7a.objects.count()
# )

# context.update({
#     'total_units_sold': total_units_sold,
#     'low_stock_count': low_stock_count,
#     'total_products': total_products,
# })
