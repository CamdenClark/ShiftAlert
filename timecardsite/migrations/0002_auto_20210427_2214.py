# Generated by Django 3.1.7 on 2021-04-27 22:14

from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('timecardsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_onboarded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(choices=[('Pacific/Midway', 'GMT-11:00 Pacific/Midway'), ('Pacific/Niue', 'GMT-11:00 Pacific/Niue'), ('Pacific/Pago_Pago', 'GMT-11:00 Pacific/Pago Pago'), ('Pacific/Honolulu', 'GMT-10:00 Pacific/Honolulu'), ('Pacific/Rarotonga', 'GMT-10:00 Pacific/Rarotonga'), ('Pacific/Tahiti', 'GMT-10:00 Pacific/Tahiti'), ('US/Hawaii', 'GMT-10:00 US/Hawaii'), ('Pacific/Marquesas', 'GMT-09:30 Pacific/Marquesas'), ('America/Adak', 'GMT-09:00 America/Adak'), ('Pacific/Gambier', 'GMT-09:00 Pacific/Gambier'), ('America/Anchorage', 'GMT-08:00 America/Anchorage'), ('America/Juneau', 'GMT-08:00 America/Juneau'), ('America/Metlakatla', 'GMT-08:00 America/Metlakatla'), ('America/Nome', 'GMT-08:00 America/Nome'), ('America/Sitka', 'GMT-08:00 America/Sitka'), ('America/Yakutat', 'GMT-08:00 America/Yakutat'), ('Pacific/Pitcairn', 'GMT-08:00 Pacific/Pitcairn'), ('US/Alaska', 'GMT-08:00 US/Alaska'), ('America/Creston', 'GMT-07:00 America/Creston'), ('America/Dawson', 'GMT-07:00 America/Dawson'), ('America/Dawson_Creek', 'GMT-07:00 America/Dawson Creek'), ('America/Fort_Nelson', 'GMT-07:00 America/Fort Nelson'), ('America/Hermosillo', 'GMT-07:00 America/Hermosillo'), ('America/Los_Angeles', 'GMT-07:00 America/Los Angeles'), ('America/Phoenix', 'GMT-07:00 America/Phoenix'), ('America/Tijuana', 'GMT-07:00 America/Tijuana'), ('America/Vancouver', 'GMT-07:00 America/Vancouver'), ('America/Whitehorse', 'GMT-07:00 America/Whitehorse'), ('Canada/Pacific', 'GMT-07:00 Canada/Pacific'), ('US/Arizona', 'GMT-07:00 US/Arizona'), ('US/Pacific', 'GMT-07:00 US/Pacific'), ('America/Belize', 'GMT-06:00 America/Belize'), ('America/Boise', 'GMT-06:00 America/Boise'), ('America/Cambridge_Bay', 'GMT-06:00 America/Cambridge Bay'), ('America/Chihuahua', 'GMT-06:00 America/Chihuahua'), ('America/Costa_Rica', 'GMT-06:00 America/Costa Rica'), ('America/Denver', 'GMT-06:00 America/Denver'), ('America/Edmonton', 'GMT-06:00 America/Edmonton'), ('America/El_Salvador', 'GMT-06:00 America/El Salvador'), ('America/Guatemala', 'GMT-06:00 America/Guatemala'), ('America/Inuvik', 'GMT-06:00 America/Inuvik'), ('America/Managua', 'GMT-06:00 America/Managua'), ('America/Mazatlan', 'GMT-06:00 America/Mazatlan'), ('America/Ojinaga', 'GMT-06:00 America/Ojinaga'), ('America/Regina', 'GMT-06:00 America/Regina'), ('America/Swift_Current', 'GMT-06:00 America/Swift Current'), ('America/Tegucigalpa', 'GMT-06:00 America/Tegucigalpa'), ('America/Yellowknife', 'GMT-06:00 America/Yellowknife'), ('Canada/Mountain', 'GMT-06:00 Canada/Mountain'), ('Pacific/Easter', 'GMT-06:00 Pacific/Easter'), ('Pacific/Galapagos', 'GMT-06:00 Pacific/Galapagos'), ('US/Mountain', 'GMT-06:00 US/Mountain'), ('America/Atikokan', 'GMT-05:00 America/Atikokan'), ('America/Bahia_Banderas', 'GMT-05:00 America/Bahia Banderas'), ('America/Bogota', 'GMT-05:00 America/Bogota'), ('America/Cancun', 'GMT-05:00 America/Cancun'), ('America/Cayman', 'GMT-05:00 America/Cayman'), ('America/Chicago', 'GMT-05:00 America/Chicago'), ('America/Eirunepe', 'GMT-05:00 America/Eirunepe'), ('America/Guayaquil', 'GMT-05:00 America/Guayaquil'), ('America/Indiana/Knox', 'GMT-05:00 America/Indiana/Knox'), ('America/Indiana/Tell_City', 'GMT-05:00 America/Indiana/Tell City'), ('America/Jamaica', 'GMT-05:00 America/Jamaica'), ('America/Lima', 'GMT-05:00 America/Lima'), ('America/Matamoros', 'GMT-05:00 America/Matamoros'), ('America/Menominee', 'GMT-05:00 America/Menominee'), ('America/Merida', 'GMT-05:00 America/Merida'), ('America/Mexico_City', 'GMT-05:00 America/Mexico City'), ('America/Monterrey', 'GMT-05:00 America/Monterrey'), ('America/North_Dakota/Beulah', 'GMT-05:00 America/North Dakota/Beulah'), ('America/North_Dakota/Center', 'GMT-05:00 America/North Dakota/Center'), ('America/North_Dakota/New_Salem', 'GMT-05:00 America/North Dakota/New Salem'), ('America/Panama', 'GMT-05:00 America/Panama'), ('America/Rainy_River', 'GMT-05:00 America/Rainy River'), ('America/Rankin_Inlet', 'GMT-05:00 America/Rankin Inlet'), ('America/Resolute', 'GMT-05:00 America/Resolute'), ('America/Rio_Branco', 'GMT-05:00 America/Rio Branco'), ('America/Winnipeg', 'GMT-05:00 America/Winnipeg'), ('Canada/Central', 'GMT-05:00 Canada/Central'), ('US/Central', 'GMT-05:00 US/Central'), ('America/Anguilla', 'GMT-04:00 America/Anguilla'), ('America/Antigua', 'GMT-04:00 America/Antigua'), ('America/Aruba', 'GMT-04:00 America/Aruba'), ('America/Asuncion', 'GMT-04:00 America/Asuncion'), ('America/Barbados', 'GMT-04:00 America/Barbados'), ('America/Blanc-Sablon', 'GMT-04:00 America/Blanc-Sablon'), ('America/Boa_Vista', 'GMT-04:00 America/Boa Vista'), ('America/Campo_Grande', 'GMT-04:00 America/Campo Grande'), ('America/Caracas', 'GMT-04:00 America/Caracas'), ('America/Cuiaba', 'GMT-04:00 America/Cuiaba'), ('America/Curacao', 'GMT-04:00 America/Curacao'), ('America/Detroit', 'GMT-04:00 America/Detroit'), ('America/Dominica', 'GMT-04:00 America/Dominica'), ('America/Grand_Turk', 'GMT-04:00 America/Grand Turk'), ('America/Grenada', 'GMT-04:00 America/Grenada'), ('America/Guadeloupe', 'GMT-04:00 America/Guadeloupe'), ('America/Guyana', 'GMT-04:00 America/Guyana'), ('America/Havana', 'GMT-04:00 America/Havana'), ('America/Indiana/Indianapolis', 'GMT-04:00 America/Indiana/Indianapolis'), ('America/Indiana/Marengo', 'GMT-04:00 America/Indiana/Marengo'), ('America/Indiana/Petersburg', 'GMT-04:00 America/Indiana/Petersburg'), ('America/Indiana/Vevay', 'GMT-04:00 America/Indiana/Vevay'), ('America/Indiana/Vincennes', 'GMT-04:00 America/Indiana/Vincennes'), ('America/Indiana/Winamac', 'GMT-04:00 America/Indiana/Winamac'), ('America/Iqaluit', 'GMT-04:00 America/Iqaluit'), ('America/Kentucky/Louisville', 'GMT-04:00 America/Kentucky/Louisville'), ('America/Kentucky/Monticello', 'GMT-04:00 America/Kentucky/Monticello'), ('America/Kralendijk', 'GMT-04:00 America/Kralendijk'), ('America/La_Paz', 'GMT-04:00 America/La Paz'), ('America/Lower_Princes', 'GMT-04:00 America/Lower Princes'), ('America/Manaus', 'GMT-04:00 America/Manaus'), ('America/Marigot', 'GMT-04:00 America/Marigot'), ('America/Martinique', 'GMT-04:00 America/Martinique'), ('America/Montserrat', 'GMT-04:00 America/Montserrat'), ('America/Nassau', 'GMT-04:00 America/Nassau'), ('America/New_York', 'GMT-04:00 America/New York'), ('America/Nipigon', 'GMT-04:00 America/Nipigon'), ('America/Pangnirtung', 'GMT-04:00 America/Pangnirtung'), ('America/Port-au-Prince', 'GMT-04:00 America/Port-au-Prince'), ('America/Port_of_Spain', 'GMT-04:00 America/Port of Spain'), ('America/Porto_Velho', 'GMT-04:00 America/Porto Velho'), ('America/Puerto_Rico', 'GMT-04:00 America/Puerto Rico'), ('America/Santiago', 'GMT-04:00 America/Santiago'), ('America/Santo_Domingo', 'GMT-04:00 America/Santo Domingo'), ('America/St_Barthelemy', 'GMT-04:00 America/St Barthelemy'), ('America/St_Kitts', 'GMT-04:00 America/St Kitts'), ('America/St_Lucia', 'GMT-04:00 America/St Lucia'), ('America/St_Thomas', 'GMT-04:00 America/St Thomas'), ('America/St_Vincent', 'GMT-04:00 America/St Vincent'), ('America/Thunder_Bay', 'GMT-04:00 America/Thunder Bay'), ('America/Toronto', 'GMT-04:00 America/Toronto'), ('America/Tortola', 'GMT-04:00 America/Tortola'), ('Canada/Eastern', 'GMT-04:00 Canada/Eastern'), ('US/Eastern', 'GMT-04:00 US/Eastern'), ('America/Araguaina', 'GMT-03:00 America/Araguaina'), ('America/Argentina/Buenos_Aires', 'GMT-03:00 America/Argentina/Buenos Aires'), ('America/Argentina/Catamarca', 'GMT-03:00 America/Argentina/Catamarca'), ('America/Argentina/Cordoba', 'GMT-03:00 America/Argentina/Cordoba'), ('America/Argentina/Jujuy', 'GMT-03:00 America/Argentina/Jujuy'), ('America/Argentina/La_Rioja', 'GMT-03:00 America/Argentina/La Rioja'), ('America/Argentina/Mendoza', 'GMT-03:00 America/Argentina/Mendoza'), ('America/Argentina/Rio_Gallegos', 'GMT-03:00 America/Argentina/Rio Gallegos'), ('America/Argentina/Salta', 'GMT-03:00 America/Argentina/Salta'), ('America/Argentina/San_Juan', 'GMT-03:00 America/Argentina/San Juan'), ('America/Argentina/San_Luis', 'GMT-03:00 America/Argentina/San Luis'), ('America/Argentina/Tucuman', 'GMT-03:00 America/Argentina/Tucuman'), ('America/Argentina/Ushuaia', 'GMT-03:00 America/Argentina/Ushuaia'), ('America/Bahia', 'GMT-03:00 America/Bahia'), ('America/Belem', 'GMT-03:00 America/Belem'), ('America/Cayenne', 'GMT-03:00 America/Cayenne'), ('America/Fortaleza', 'GMT-03:00 America/Fortaleza'), ('America/Glace_Bay', 'GMT-03:00 America/Glace Bay'), ('America/Goose_Bay', 'GMT-03:00 America/Goose Bay'), ('America/Halifax', 'GMT-03:00 America/Halifax'), ('America/Maceio', 'GMT-03:00 America/Maceio'), ('America/Moncton', 'GMT-03:00 America/Moncton'), ('America/Montevideo', 'GMT-03:00 America/Montevideo'), ('America/Paramaribo', 'GMT-03:00 America/Paramaribo'), ('America/Punta_Arenas', 'GMT-03:00 America/Punta Arenas'), ('America/Recife', 'GMT-03:00 America/Recife'), ('America/Santarem', 'GMT-03:00 America/Santarem'), ('America/Sao_Paulo', 'GMT-03:00 America/Sao Paulo'), ('America/Thule', 'GMT-03:00 America/Thule'), ('Antarctica/Palmer', 'GMT-03:00 Antarctica/Palmer'), ('Antarctica/Rothera', 'GMT-03:00 Antarctica/Rothera'), ('Atlantic/Bermuda', 'GMT-03:00 Atlantic/Bermuda'), ('Atlantic/Stanley', 'GMT-03:00 Atlantic/Stanley'), ('Canada/Atlantic', 'GMT-03:00 Canada/Atlantic'), ('America/St_Johns', 'GMT-02:30 America/St Johns'), ('Canada/Newfoundland', 'GMT-02:30 Canada/Newfoundland'), ('America/Miquelon', 'GMT-02:00 America/Miquelon'), ('America/Noronha', 'GMT-02:00 America/Noronha'), ('America/Nuuk', 'GMT-02:00 America/Nuuk'), ('Atlantic/South_Georgia', 'GMT-02:00 Atlantic/South Georgia'), ('Atlantic/Cape_Verde', 'GMT-01:00 Atlantic/Cape Verde'), ('Africa/Abidjan', 'GMT+00:00 Africa/Abidjan'), ('Africa/Accra', 'GMT+00:00 Africa/Accra'), ('Africa/Bamako', 'GMT+00:00 Africa/Bamako'), ('Africa/Banjul', 'GMT+00:00 Africa/Banjul'), ('Africa/Bissau', 'GMT+00:00 Africa/Bissau'), ('Africa/Casablanca', 'GMT+00:00 Africa/Casablanca'), ('Africa/Conakry', 'GMT+00:00 Africa/Conakry'), ('Africa/Dakar', 'GMT+00:00 Africa/Dakar'), ('Africa/El_Aaiun', 'GMT+00:00 Africa/El Aaiun'), ('Africa/Freetown', 'GMT+00:00 Africa/Freetown'), ('Africa/Lome', 'GMT+00:00 Africa/Lome'), ('Africa/Monrovia', 'GMT+00:00 Africa/Monrovia'), ('Africa/Nouakchott', 'GMT+00:00 Africa/Nouakchott'), ('Africa/Ouagadougou', 'GMT+00:00 Africa/Ouagadougou'), ('Africa/Sao_Tome', 'GMT+00:00 Africa/Sao Tome'), ('America/Danmarkshavn', 'GMT+00:00 America/Danmarkshavn'), ('America/Scoresbysund', 'GMT+00:00 America/Scoresbysund'), ('Atlantic/Azores', 'GMT+00:00 Atlantic/Azores'), ('Atlantic/Reykjavik', 'GMT+00:00 Atlantic/Reykjavik'), ('Atlantic/St_Helena', 'GMT+00:00 Atlantic/St Helena'), ('GMT', 'GMT+00:00 GMT'), ('UTC', 'GMT+00:00 UTC'), ('Africa/Algiers', 'GMT+01:00 Africa/Algiers'), ('Africa/Bangui', 'GMT+01:00 Africa/Bangui'), ('Africa/Brazzaville', 'GMT+01:00 Africa/Brazzaville'), ('Africa/Douala', 'GMT+01:00 Africa/Douala'), ('Africa/Kinshasa', 'GMT+01:00 Africa/Kinshasa'), ('Africa/Lagos', 'GMT+01:00 Africa/Lagos'), ('Africa/Libreville', 'GMT+01:00 Africa/Libreville'), ('Africa/Luanda', 'GMT+01:00 Africa/Luanda'), ('Africa/Malabo', 'GMT+01:00 Africa/Malabo'), ('Africa/Ndjamena', 'GMT+01:00 Africa/Ndjamena'), ('Africa/Niamey', 'GMT+01:00 Africa/Niamey'), ('Africa/Porto-Novo', 'GMT+01:00 Africa/Porto-Novo'), ('Africa/Tunis', 'GMT+01:00 Africa/Tunis'), ('Atlantic/Canary', 'GMT+01:00 Atlantic/Canary'), ('Atlantic/Faroe', 'GMT+01:00 Atlantic/Faroe'), ('Atlantic/Madeira', 'GMT+01:00 Atlantic/Madeira'), ('Europe/Dublin', 'GMT+01:00 Europe/Dublin'), ('Europe/Guernsey', 'GMT+01:00 Europe/Guernsey'), ('Europe/Isle_of_Man', 'GMT+01:00 Europe/Isle of Man'), ('Europe/Jersey', 'GMT+01:00 Europe/Jersey'), ('Europe/Lisbon', 'GMT+01:00 Europe/Lisbon'), ('Europe/London', 'GMT+01:00 Europe/London'), ('Africa/Blantyre', 'GMT+02:00 Africa/Blantyre'), ('Africa/Bujumbura', 'GMT+02:00 Africa/Bujumbura'), ('Africa/Cairo', 'GMT+02:00 Africa/Cairo'), ('Africa/Ceuta', 'GMT+02:00 Africa/Ceuta'), ('Africa/Gaborone', 'GMT+02:00 Africa/Gaborone'), ('Africa/Harare', 'GMT+02:00 Africa/Harare'), ('Africa/Johannesburg', 'GMT+02:00 Africa/Johannesburg'), ('Africa/Juba', 'GMT+02:00 Africa/Juba'), ('Africa/Khartoum', 'GMT+02:00 Africa/Khartoum'), ('Africa/Kigali', 'GMT+02:00 Africa/Kigali'), ('Africa/Lubumbashi', 'GMT+02:00 Africa/Lubumbashi'), ('Africa/Lusaka', 'GMT+02:00 Africa/Lusaka'), ('Africa/Maputo', 'GMT+02:00 Africa/Maputo'), ('Africa/Maseru', 'GMT+02:00 Africa/Maseru'), ('Africa/Mbabane', 'GMT+02:00 Africa/Mbabane'), ('Africa/Tripoli', 'GMT+02:00 Africa/Tripoli'), ('Africa/Windhoek', 'GMT+02:00 Africa/Windhoek'), ('Antarctica/Troll', 'GMT+02:00 Antarctica/Troll'), ('Arctic/Longyearbyen', 'GMT+02:00 Arctic/Longyearbyen'), ('Europe/Amsterdam', 'GMT+02:00 Europe/Amsterdam'), ('Europe/Andorra', 'GMT+02:00 Europe/Andorra'), ('Europe/Belgrade', 'GMT+02:00 Europe/Belgrade'), ('Europe/Berlin', 'GMT+02:00 Europe/Berlin'), ('Europe/Bratislava', 'GMT+02:00 Europe/Bratislava'), ('Europe/Brussels', 'GMT+02:00 Europe/Brussels'), ('Europe/Budapest', 'GMT+02:00 Europe/Budapest'), ('Europe/Busingen', 'GMT+02:00 Europe/Busingen'), ('Europe/Copenhagen', 'GMT+02:00 Europe/Copenhagen'), ('Europe/Gibraltar', 'GMT+02:00 Europe/Gibraltar'), ('Europe/Kaliningrad', 'GMT+02:00 Europe/Kaliningrad'), ('Europe/Ljubljana', 'GMT+02:00 Europe/Ljubljana'), ('Europe/Luxembourg', 'GMT+02:00 Europe/Luxembourg'), ('Europe/Madrid', 'GMT+02:00 Europe/Madrid'), ('Europe/Malta', 'GMT+02:00 Europe/Malta'), ('Europe/Monaco', 'GMT+02:00 Europe/Monaco'), ('Europe/Oslo', 'GMT+02:00 Europe/Oslo'), ('Europe/Paris', 'GMT+02:00 Europe/Paris'), ('Europe/Podgorica', 'GMT+02:00 Europe/Podgorica'), ('Europe/Prague', 'GMT+02:00 Europe/Prague'), ('Europe/Rome', 'GMT+02:00 Europe/Rome'), ('Europe/San_Marino', 'GMT+02:00 Europe/San Marino'), ('Europe/Sarajevo', 'GMT+02:00 Europe/Sarajevo'), ('Europe/Skopje', 'GMT+02:00 Europe/Skopje'), ('Europe/Stockholm', 'GMT+02:00 Europe/Stockholm'), ('Europe/Tirane', 'GMT+02:00 Europe/Tirane'), ('Europe/Vaduz', 'GMT+02:00 Europe/Vaduz'), ('Europe/Vatican', 'GMT+02:00 Europe/Vatican'), ('Europe/Vienna', 'GMT+02:00 Europe/Vienna'), ('Europe/Warsaw', 'GMT+02:00 Europe/Warsaw'), ('Europe/Zagreb', 'GMT+02:00 Europe/Zagreb'), ('Europe/Zurich', 'GMT+02:00 Europe/Zurich'), ('Africa/Addis_Ababa', 'GMT+03:00 Africa/Addis Ababa'), ('Africa/Asmara', 'GMT+03:00 Africa/Asmara'), ('Africa/Dar_es_Salaam', 'GMT+03:00 Africa/Dar es Salaam'), ('Africa/Djibouti', 'GMT+03:00 Africa/Djibouti'), ('Africa/Kampala', 'GMT+03:00 Africa/Kampala'), ('Africa/Mogadishu', 'GMT+03:00 Africa/Mogadishu'), ('Africa/Nairobi', 'GMT+03:00 Africa/Nairobi'), ('Antarctica/Syowa', 'GMT+03:00 Antarctica/Syowa'), ('Asia/Aden', 'GMT+03:00 Asia/Aden'), ('Asia/Amman', 'GMT+03:00 Asia/Amman'), ('Asia/Baghdad', 'GMT+03:00 Asia/Baghdad'), ('Asia/Bahrain', 'GMT+03:00 Asia/Bahrain'), ('Asia/Beirut', 'GMT+03:00 Asia/Beirut'), ('Asia/Damascus', 'GMT+03:00 Asia/Damascus'), ('Asia/Famagusta', 'GMT+03:00 Asia/Famagusta'), ('Asia/Gaza', 'GMT+03:00 Asia/Gaza'), ('Asia/Hebron', 'GMT+03:00 Asia/Hebron'), ('Asia/Jerusalem', 'GMT+03:00 Asia/Jerusalem'), ('Asia/Kuwait', 'GMT+03:00 Asia/Kuwait'), ('Asia/Nicosia', 'GMT+03:00 Asia/Nicosia'), ('Asia/Qatar', 'GMT+03:00 Asia/Qatar'), ('Asia/Riyadh', 'GMT+03:00 Asia/Riyadh'), ('Europe/Athens', 'GMT+03:00 Europe/Athens'), ('Europe/Bucharest', 'GMT+03:00 Europe/Bucharest'), ('Europe/Chisinau', 'GMT+03:00 Europe/Chisinau'), ('Europe/Helsinki', 'GMT+03:00 Europe/Helsinki'), ('Europe/Istanbul', 'GMT+03:00 Europe/Istanbul'), ('Europe/Kiev', 'GMT+03:00 Europe/Kiev'), ('Europe/Kirov', 'GMT+03:00 Europe/Kirov'), ('Europe/Mariehamn', 'GMT+03:00 Europe/Mariehamn'), ('Europe/Minsk', 'GMT+03:00 Europe/Minsk'), ('Europe/Moscow', 'GMT+03:00 Europe/Moscow'), ('Europe/Riga', 'GMT+03:00 Europe/Riga'), ('Europe/Simferopol', 'GMT+03:00 Europe/Simferopol'), ('Europe/Sofia', 'GMT+03:00 Europe/Sofia'), ('Europe/Tallinn', 'GMT+03:00 Europe/Tallinn'), ('Europe/Uzhgorod', 'GMT+03:00 Europe/Uzhgorod'), ('Europe/Vilnius', 'GMT+03:00 Europe/Vilnius'), ('Europe/Volgograd', 'GMT+03:00 Europe/Volgograd'), ('Europe/Zaporozhye', 'GMT+03:00 Europe/Zaporozhye'), ('Indian/Antananarivo', 'GMT+03:00 Indian/Antananarivo'), ('Indian/Comoro', 'GMT+03:00 Indian/Comoro'), ('Indian/Mayotte', 'GMT+03:00 Indian/Mayotte'), ('Asia/Baku', 'GMT+04:00 Asia/Baku'), ('Asia/Dubai', 'GMT+04:00 Asia/Dubai'), ('Asia/Muscat', 'GMT+04:00 Asia/Muscat'), ('Asia/Tbilisi', 'GMT+04:00 Asia/Tbilisi'), ('Asia/Yerevan', 'GMT+04:00 Asia/Yerevan'), ('Europe/Astrakhan', 'GMT+04:00 Europe/Astrakhan'), ('Europe/Samara', 'GMT+04:00 Europe/Samara'), ('Europe/Saratov', 'GMT+04:00 Europe/Saratov'), ('Europe/Ulyanovsk', 'GMT+04:00 Europe/Ulyanovsk'), ('Indian/Mahe', 'GMT+04:00 Indian/Mahe'), ('Indian/Mauritius', 'GMT+04:00 Indian/Mauritius'), ('Indian/Reunion', 'GMT+04:00 Indian/Reunion'), ('Asia/Kabul', 'GMT+04:30 Asia/Kabul'), ('Asia/Tehran', 'GMT+04:30 Asia/Tehran'), ('Antarctica/Mawson', 'GMT+05:00 Antarctica/Mawson'), ('Asia/Aqtau', 'GMT+05:00 Asia/Aqtau'), ('Asia/Aqtobe', 'GMT+05:00 Asia/Aqtobe'), ('Asia/Ashgabat', 'GMT+05:00 Asia/Ashgabat'), ('Asia/Atyrau', 'GMT+05:00 Asia/Atyrau'), ('Asia/Dushanbe', 'GMT+05:00 Asia/Dushanbe'), ('Asia/Karachi', 'GMT+05:00 Asia/Karachi'), ('Asia/Oral', 'GMT+05:00 Asia/Oral'), ('Asia/Qyzylorda', 'GMT+05:00 Asia/Qyzylorda'), ('Asia/Samarkand', 'GMT+05:00 Asia/Samarkand'), ('Asia/Tashkent', 'GMT+05:00 Asia/Tashkent'), ('Asia/Yekaterinburg', 'GMT+05:00 Asia/Yekaterinburg'), ('Indian/Kerguelen', 'GMT+05:00 Indian/Kerguelen'), ('Indian/Maldives', 'GMT+05:00 Indian/Maldives'), ('Asia/Colombo', 'GMT+05:30 Asia/Colombo'), ('Asia/Kolkata', 'GMT+05:30 Asia/Kolkata'), ('Asia/Kathmandu', 'GMT+05:45 Asia/Kathmandu'), ('Antarctica/Vostok', 'GMT+06:00 Antarctica/Vostok'), ('Asia/Almaty', 'GMT+06:00 Asia/Almaty'), ('Asia/Bishkek', 'GMT+06:00 Asia/Bishkek'), ('Asia/Dhaka', 'GMT+06:00 Asia/Dhaka'), ('Asia/Omsk', 'GMT+06:00 Asia/Omsk'), ('Asia/Qostanay', 'GMT+06:00 Asia/Qostanay'), ('Asia/Thimphu', 'GMT+06:00 Asia/Thimphu'), ('Asia/Urumqi', 'GMT+06:00 Asia/Urumqi'), ('Indian/Chagos', 'GMT+06:00 Indian/Chagos'), ('Asia/Yangon', 'GMT+06:30 Asia/Yangon'), ('Indian/Cocos', 'GMT+06:30 Indian/Cocos'), ('Antarctica/Davis', 'GMT+07:00 Antarctica/Davis'), ('Asia/Bangkok', 'GMT+07:00 Asia/Bangkok'), ('Asia/Barnaul', 'GMT+07:00 Asia/Barnaul'), ('Asia/Ho_Chi_Minh', 'GMT+07:00 Asia/Ho Chi Minh'), ('Asia/Hovd', 'GMT+07:00 Asia/Hovd'), ('Asia/Jakarta', 'GMT+07:00 Asia/Jakarta'), ('Asia/Krasnoyarsk', 'GMT+07:00 Asia/Krasnoyarsk'), ('Asia/Novokuznetsk', 'GMT+07:00 Asia/Novokuznetsk'), ('Asia/Novosibirsk', 'GMT+07:00 Asia/Novosibirsk'), ('Asia/Phnom_Penh', 'GMT+07:00 Asia/Phnom Penh'), ('Asia/Pontianak', 'GMT+07:00 Asia/Pontianak'), ('Asia/Tomsk', 'GMT+07:00 Asia/Tomsk'), ('Asia/Vientiane', 'GMT+07:00 Asia/Vientiane'), ('Indian/Christmas', 'GMT+07:00 Indian/Christmas'), ('Asia/Brunei', 'GMT+08:00 Asia/Brunei'), ('Asia/Choibalsan', 'GMT+08:00 Asia/Choibalsan'), ('Asia/Hong_Kong', 'GMT+08:00 Asia/Hong Kong'), ('Asia/Irkutsk', 'GMT+08:00 Asia/Irkutsk'), ('Asia/Kuala_Lumpur', 'GMT+08:00 Asia/Kuala Lumpur'), ('Asia/Kuching', 'GMT+08:00 Asia/Kuching'), ('Asia/Macau', 'GMT+08:00 Asia/Macau'), ('Asia/Makassar', 'GMT+08:00 Asia/Makassar'), ('Asia/Manila', 'GMT+08:00 Asia/Manila'), ('Asia/Shanghai', 'GMT+08:00 Asia/Shanghai'), ('Asia/Singapore', 'GMT+08:00 Asia/Singapore'), ('Asia/Taipei', 'GMT+08:00 Asia/Taipei'), ('Asia/Ulaanbaatar', 'GMT+08:00 Asia/Ulaanbaatar'), ('Australia/Perth', 'GMT+08:00 Australia/Perth'), ('Australia/Eucla', 'GMT+08:45 Australia/Eucla'), ('Asia/Chita', 'GMT+09:00 Asia/Chita'), ('Asia/Dili', 'GMT+09:00 Asia/Dili'), ('Asia/Jayapura', 'GMT+09:00 Asia/Jayapura'), ('Asia/Khandyga', 'GMT+09:00 Asia/Khandyga'), ('Asia/Pyongyang', 'GMT+09:00 Asia/Pyongyang'), ('Asia/Seoul', 'GMT+09:00 Asia/Seoul'), ('Asia/Tokyo', 'GMT+09:00 Asia/Tokyo'), ('Asia/Yakutsk', 'GMT+09:00 Asia/Yakutsk'), ('Pacific/Palau', 'GMT+09:00 Pacific/Palau'), ('Australia/Adelaide', 'GMT+09:30 Australia/Adelaide'), ('Australia/Broken_Hill', 'GMT+09:30 Australia/Broken Hill'), ('Australia/Darwin', 'GMT+09:30 Australia/Darwin'), ('Antarctica/DumontDUrville', 'GMT+10:00 Antarctica/DumontDUrville'), ('Antarctica/Macquarie', 'GMT+10:00 Antarctica/Macquarie'), ('Asia/Ust-Nera', 'GMT+10:00 Asia/Ust-Nera'), ('Asia/Vladivostok', 'GMT+10:00 Asia/Vladivostok'), ('Australia/Brisbane', 'GMT+10:00 Australia/Brisbane'), ('Australia/Hobart', 'GMT+10:00 Australia/Hobart'), ('Australia/Lindeman', 'GMT+10:00 Australia/Lindeman'), ('Australia/Melbourne', 'GMT+10:00 Australia/Melbourne'), ('Australia/Sydney', 'GMT+10:00 Australia/Sydney'), ('Pacific/Chuuk', 'GMT+10:00 Pacific/Chuuk'), ('Pacific/Guam', 'GMT+10:00 Pacific/Guam'), ('Pacific/Port_Moresby', 'GMT+10:00 Pacific/Port Moresby'), ('Pacific/Saipan', 'GMT+10:00 Pacific/Saipan'), ('Australia/Lord_Howe', 'GMT+10:30 Australia/Lord Howe'), ('Antarctica/Casey', 'GMT+11:00 Antarctica/Casey'), ('Asia/Magadan', 'GMT+11:00 Asia/Magadan'), ('Asia/Sakhalin', 'GMT+11:00 Asia/Sakhalin'), ('Asia/Srednekolymsk', 'GMT+11:00 Asia/Srednekolymsk'), ('Pacific/Bougainville', 'GMT+11:00 Pacific/Bougainville'), ('Pacific/Efate', 'GMT+11:00 Pacific/Efate'), ('Pacific/Guadalcanal', 'GMT+11:00 Pacific/Guadalcanal'), ('Pacific/Kosrae', 'GMT+11:00 Pacific/Kosrae'), ('Pacific/Norfolk', 'GMT+11:00 Pacific/Norfolk'), ('Pacific/Noumea', 'GMT+11:00 Pacific/Noumea'), ('Pacific/Pohnpei', 'GMT+11:00 Pacific/Pohnpei'), ('Antarctica/McMurdo', 'GMT+12:00 Antarctica/McMurdo'), ('Asia/Anadyr', 'GMT+12:00 Asia/Anadyr'), ('Asia/Kamchatka', 'GMT+12:00 Asia/Kamchatka'), ('Pacific/Auckland', 'GMT+12:00 Pacific/Auckland'), ('Pacific/Fiji', 'GMT+12:00 Pacific/Fiji'), ('Pacific/Funafuti', 'GMT+12:00 Pacific/Funafuti'), ('Pacific/Kwajalein', 'GMT+12:00 Pacific/Kwajalein'), ('Pacific/Majuro', 'GMT+12:00 Pacific/Majuro'), ('Pacific/Nauru', 'GMT+12:00 Pacific/Nauru'), ('Pacific/Tarawa', 'GMT+12:00 Pacific/Tarawa'), ('Pacific/Wake', 'GMT+12:00 Pacific/Wake'), ('Pacific/Wallis', 'GMT+12:00 Pacific/Wallis'), ('Pacific/Chatham', 'GMT+12:45 Pacific/Chatham'), ('Pacific/Apia', 'GMT+13:00 Pacific/Apia'), ('Pacific/Enderbury', 'GMT+13:00 Pacific/Enderbury'), ('Pacific/Fakaofo', 'GMT+13:00 Pacific/Fakaofo'), ('Pacific/Tongatapu', 'GMT+13:00 Pacific/Tongatapu'), ('Pacific/Kiritimati', 'GMT+14:00 Pacific/Kiritimati')], default='America/Boise'),
        ),
    ]