from typing import Dict, List
from data_models import Product, Color

def get_top_n_products(cluster1: int, cluster2: int, n: int, fashion_data: Dict) -> List[Product]:
  assert n >= 0, "n must be positive"
  
  results = []
  for k, v in fashion_data.items():
    if v['cluster_C1'] is None or v['cluster_C2'] is None:
      continue
    
    if int(v['cluster_C1']) == cluster1 and int(v['cluster_C2']) == cluster2:
      results.append(Product(image=v['image_id'],
                             pattern=v['pttrn_type'],
                             avg_rating=v['avg_rating'],
                             n_reviews=v['no_of_reviews'],
                             color3=Color(r=v['Color_3'][0], g=v['Color_3'][1], b=v['Color_3'][2]),
                             trend=v['Trend']))
  return sorted(results, key=lambda p: p.trend, reverse=True)[:n]