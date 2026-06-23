from pathlib import Path

base = Path('templates/tmp_transporter')
replacements = {
    'index.html': '/transportapp/index_view/',
    'assigned_shipments.html': '/transportapp/assigned_view/',
    'shipment_details.html': '/transportapp/shipment_view/',
    'vehicles.html': '/transportapp/vehicle_view/',
    'drivers.html': '/transportapp/drivers_view/',
    'routes.html': '/transportapp/routes_view/',
    'pod.html': '/transportapp/pod_view/',
    'earnings.html': '/transportapp/earnings_view/',
    'settings.html': '/transportapp/settings_view/',
}

for path in base.glob('*.html'):
    text = path.read_text(encoding='utf-8')
    orig = text
    for old, new in replacements.items():
        text = text.replace(f'href="{old}"', f'href="{new}"')
    if text != orig:
        path.write_text(text, encoding='utf-8')
        print(f'Updated {path.name}')
