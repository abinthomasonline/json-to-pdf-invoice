import argparse
import json
from datetime import datetime
import pdfkit

def main(input_json_path, output_pdf_path):
    with open(input_json_path, 'r') as f:
        data = json.load(f)
    package = data['packages'][0]

    with open('template.html', 'r') as f:
        template = f.read()
    template = template.format(
        pin=package["pin"],
        cd=datetime.strptime(package["cd"][:-4], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d %H: %M: %S"), 
        snm=package["snm"],
        barcode=package["barcode"],
        pt=package["pt"],
        rs=round(package["rs"]),
        destination=package["destination"],
        prd=package["prd"],
        sadd=package["sadd"],
        oid_barcode=package["oid_barcode"],
        radd=package["radd"],
        address=package["address"],
        name=package["name"],
        delhivery_logo=package["delhivery_logo"],
        sort_code=package["sort_code"],
    )

    with open('style.css', 'r') as f:
        style = f.read()
    template += '<style>{}</style>'.format(style)

    pdfkit.from_string(template, output_pdf_path, options={'enable-local-file-access': ''})

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_json_path', type=str, default='sample.json')
    parser.add_argument('--output_pdf_path', type=str, default='sample.pdf')
    args = parser.parse_args()

    main(args.input_json_path, args.output_pdf_path)
