# import pandas as pd
# import random

# # Dữ liệu tên và thành phố cho từng quốc gia
# country_data = {
#    "Vietnam": {
#         "names": [
#             "An Vo", "Nam Le", "Hoang Nguyen", "Mai Anh Le", "Thi Nguyen",
#             "Trung Nguyen", "Hai Nguyen", "Hoa Nguyen", "Thao Nguyen", "Huong Nguyen",
#             "Minh Tuan", "Thanh Hoa", "Anh Tu", "Quang Hieu", "Thu Ha",
#             "Linh Dao", "Kien Trung", "Bich Phuong", "Bao Chau", "Thuy Linh",
#             "Duy Tan", "Mai Lan", "Quyen Trang", "Ngoc Lan", "Thanh Mai",
#             "Lan Anh", "Gia Bao", "Hoang Minh", "Tuan Anh", "Bao Vy",
#             "Thanh Phuc", "Quoc Duy", "Bich Thao", "Bao Quyen", "Anh Tho",
#             "Truong Hieu", "Thi Thanh", "Minh Hieu", "Lan Quyen", "Duong Minh",
#             "Thien Kieu", "Tuan Kien", "Hong Dao", "Tram Anh", "Duc Minh",
#             "Anh Quyen", "Thanh Son", "Trung Son", "Nhat Thao", "Nguyen Lan",
#             "Minh Quyen", "Thu Thao", "Khong Hieu", "Thi Mai", "Hoang Bao",
#             "Mai Linh", "Tuan Khoi", "Bich Minh", "Mai Quyen", "Truong Anh",
#             "Thuy An", "Nguyen Thanh", "Tuan Minh", "Bao Linh", "Khuyen Thu",
#             "Anh Hoa", "Thanh Thi", "Hong Minh", "Khong Lan", "Hoang Kieu",
#             "Thien Hoa", "Thanh Mai", "Nguyen Thi", "Gia Bao", "Minh Lan",
#             "Duc Anh", "Mai Trang", "Anh Thi", "Nhat Hoa", "Quoc Bao",
#             "Thu Kieu", "Truong Quyen", "Thi Bao", "Hieu Hoa", "Mai Minh",
#             "Thi Lan", "Trung Bao", "Thanh Hoang", "Truong Thu", "Minh Quoc",
#             "Nguyen Tuan", "Anh Tuan", "Linh Mai", "Thuy Kieu", "Duy Lan",
#             "Thanh Linh", "Bich Thu", "Thu Mai", "Tram Minh", "Bao Hoa",
#             "Quyen Linh", "Truong Thao", "Thi Bao", "Duc Kien", "An Mai",
#             "Thi Bao", "Mai Son", "Hoang Minh", "Thanh Kien", "Thao Quyen",
#             "Mai Phuong", "Bao An", "Truong Hoa", "Tuan Quyen", "Thi Son"
#         ],
#         "cities": ["Hà Nội", "Hồ Chí Minh", "Đà Nẵng", "Cần Thơ", "Nha Trang"],
#         "ethnic_groups": ["Kinh", "Tay", "Thai", "Muong", "H'mong"]
#     },
#     "China": {
#         "names": [
#             "Wei", "Jia", "Xia", "Ling", "Tao", "Zhang Wei", "Li Jia", "Wang Xia",
#             "Liu Ling", "Chen Tao", "Yang Xiu", "Zhou Qian", "Sun Jun", "Xu Dong",
#             "Hu Yun", "He Mei", "Gao Lei", "Li Ying", "Zhang Qi", "Liu Feng",
#             "Chen Ji", "Wang Min", "Yang Yun", "Zhou Shan", "Sun Jian", "Xu Ling",
#             "Liang Ying", "Wu Jian", "Li Hua", "Zhang Ping", "Liu Tao", "Xu Han",
#             "Hu Xin", "He Jing", "Gao Jun", "Li Hong", "Zhao Lei", "Wang Ji",
#             "Yang Qing", "Zhou Wei", "Sun Yun", "Xu Jie", "Liang Mei", "Wu Lan",
#             "Li Ling", "Zhang Min", "Liu Jian", "Chen Mei", "Wang Qi", "Yang Wei",
#             "Zhou Yun", "Sun Jian", "Xu Qian", "Li Ping", "Gao Hong", "Liang Ji",
#             "Wu Jia", "Liang Tao", "Zhao Ming", "Yang Lei", "Zhou Fang", "Sun Qi",
#             "Xu Ying", "Liang Qian", "Li Hao", "Wang Zhi", "Gao Ying", "He Min",
#             "Li Zhen", "Zhao Wei", "Wang Hui", "Yang Yun", "Zhou Ming", "Xu Wei",
#             "Li Yan", "Liang Fen", "Wu Zhen", "Zhang Hua", "Liu Hong", "Chen Feng",
#             "Wang Wei", "Yang Ling", "Zhou Ying", "Sun Hong", "Xu Jing", "Liang Jian",
#             "Li Qian", "Wang Yu", "Gao Hui", "Zhao Ling", "Zhou Zhen", "Yang Lin",
#             "Sun Fen", "Xu Zhi", "Liang Yun", "Wu Ming", "Zhang Qi", "Liu Min"
#         ],
#         "cities": ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu"],
#         "ethnic_groups": ["Han", "Tibetan", "Uighur", "Zhuang", "Mongol"]
#     },
#     "United States of America": {
#         "names": [
#             "John", "Mary", "Alice", "Bob", "Eve", "William", "Olivia", "James", "Isabella", "Sophia",
#             "Benjamin", "Charlotte", "Alexander", "Amelia", "Elijah", "Mia", "David", "Harper", "Henry",
#             "Liam", "Emily", "Jack", "Grace", "Samuel", "Madeline", "Matthew", "Ava", "Christopher", "Ella",
#             "Andrew", "Zoe", "Michael", "Lily", "Joseph", "Sophie", "Daniel", "Eleanor", "Isaac", "Leah",
#             "Lucas", "Addison", "Thomas", "Chloe", "Ethan", "Victoria", "Daniel", "Ruby", "Oliver", "Megan",
#             "Elise", "William", "Jackson", "Samantha", "Noah", "Amos", "Emma", "Tyler", "Sadie", "Caleb",
#             "Eliza", "Charlotte", "Levi", "Jackson", "Johnathan", "Aiden", "Sienna", "Owen", "Aiden", "Kayla",
#             "Connor", "Emily", "Jackie", "Alfred", "Tyson", "Madelyn", "Charles", "Max", "Maddie", "Oscar",
#             "Caleb", "Addison", "Matthew", "Harper", "Charlie", "Mason", "Ella", "Jayden", "Addison", "Layla",
#             "Joshua", "Aaron", "Zane", "Aiden", "Layla", "Miles", "Riley", "Noah", "Piper", "Elliot", "Lola",
#             "Cooper", "Sadie", "Victor", "Jasmine", "Dylan", "Mikayla", "Evan", "Quinn", "Avery", "Ian", "Sophie"
#         ],
#         "cities": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
#         "ethnic_groups": ["White", "Black or African American", "Hispanic or Latino", "Asian", "Native American"]
#     },
#     "Brazil": {
#         "names": [
#             "João", "Maria", "Ana", "Pedro", "Carlos", "Gabriel", "Rafael", "Lucas", "Fernanda", "Beatriz",
#             "Júlia", "Paula", "Camila", "Juliana", "Mariana", "Antonio", "Rodrigo", "Lucas", "Felipe", "André",
#             "Larissa", "Danielle", "Eduarda", "Aline", "José", "Vitor", "Monique", "Carlos", "Fernando", "Alessandra",
#             "Roberta", "Ricardo", "Simone", "Tatiane", "Larissa", "Leonardo", "Fabio", "Tiago", "Eliane", "Bruna",
#             "Rosa", "Gustavo", "Luana", "Aline", "Luciana", "Camila", "Bruna", "Robson", "David", "Luciano",
#             "Carlos", "Thiago", "Juliana", "Eliane", "Lucia", "Marcos", "Denise", "Paula", "Amanda", "Letícia",
#             "Murilo", "Diana", "Joana", "Sandra", "Nathalia", "Tatiane", "Daniela", "Rogério", "Priscila", "Débora",
#             "Cristiane", "Carlos", "Gustavo", "Fabio", "Renato", "Vânia", "Ricardo", "Ana Paula", "Adriana",
#             "Sandro", "Evelyn", "Tainá", "João Pedro", "Tatiane", "Vanessa", "Kátia", "Cíntia", "Silvia",
#             "Beatriz", "Ana Carolina", "Ricardo", "Murilo", "Felipe", "Marco", "Brenda", "Davi", "Igor", "Gustavo",
#             "Isabel", "Débora", "Thiago", "Rita", "Luciana", "Márcia", "Gilberto", "Paula", "Jussara", "César"
#         ],
#         "cities": ["São Paulo", "Rio de Janeiro", "Salvador", "Brasília", "Fortaleza"],
#         "ethnic_groups": ["White", "Pardo", "Black", "Asian", "Indigenous"]
#     },
#     "India": {
#         "names": [
#             "Amit", "Priya", "Ravi", "Anjali", "Rajesh", "Neha", "Suresh", "Vinay", "Shalini", "Kiran",
#             "Sandeep", "Pooja", "Deepak", "Vandana", "Rina", "Ajay", "Vikram", "Meena", "Nitin", "Jyoti",
#             "Rahul", "Sonali", "Tarun", "Shivani", "Ruchi", "Brijesh", "Nikita", "Manoj", "Ankita", "Subhash",
#             "Madhuri", "Krishna", "Richa", "Rohit", "Rina", "Alok", "Swati", "Ashok", "Kavita", "Suman",
#             "Harish", "Komal", "Raghav", "Nisha", "Yogesh", "Chandrika", "Satish", "Rajat", "Suman",
#             "Jaya", "Gurpreet", "Karan", "Sandeep", "Sarita", "Neeraj", "Manish", "Parveen", "Vinita",
#             "Madhuri", "Vineet", "Sheetal", "Sandeep", "Maya", "Tejas", "Neha", "Usha", "Ajit", "Pankaj",
#             "Amita", "Vandana", "Parul", "Anshika", "Vikrant", "Nidhi", "Vikas", "Shailendra", "Preeti",
#             "Pooja", "Bhawana", "Rajeev", "Seema", "Bhupendra", "Vinod", "Amitabh", "Meena", "Indira",
#             "Ankit", "Priya", "Tanu", "Amandeep", "Prashant", "Poonam", "Sanjay", "Dinesh", "Sushma",
#             "Sunil", "Alka", "Ravindra", "Laxmi", "Harvinder", "Aarti"
#         ],
#         "cities": ["Mumbai", "Delhi", "Bangalore", "Kolkata", "Chennai"],
#         "ethnic_groups": ["Hindu", "Muslim", "Sikh", "Christian", "Other"]
#     },
#     "Germany": {
#         "names": [
#             "Johann", "Lena", "Mika", "Klara", "Max", "Sophie", "Nina", "Jana", "Felix", "Anna",
#             "Ben", "Lukas", "Paula", "Emma", "Moritz", "Lena", "Jonas", "Mia", "Tim", "Hannah",
#             "Tom", "Lea", "Luca", "Charlotte", "Samuel", "Elena", "Maximilian", "Lina", "Matthias",
#             "Alina", "Jakob", "Maya", "Noah", "Sophia", "Friedrich", "Emil", "Celine", "Louis",
#             "Marlene", "Johannes", "Mia", "Johanna", "Nico", "Sven", "Paula", "Simon", "Isabel",
#             "Matti", "Fiona", "Carla", "Victor", "Helen", "Marie", "Peter", "Freya", "Lena",
#             "Alexander", "Clara", "Diana", "Moritz", "Leonie", "Armin", "Charlotte", "Lukas", "Karl",
#             "Rafael", "Lukas", "Tim", "Matthias", "Lilian", "Olivia", "Jonas", "Henry", "Felicitas",
#             "Niels", "Saskia", "Klara", "Eva", "Benedikt", "Silvia", "Julia", "Felix", "Andreas",
#             "Malte", "Clara", "Arne", "Emma", "Melina", "Pascal", "Birgit", "Olaf", "Friedrich",
#             "Gabriela", "Willy", "Anja", "Lisa", "Sabine", "Benedikt", "David"
#         ],
#         "cities": ["Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne"],
#         "ethnic_groups": ["German", "Turkish", "Kurdish", "Polish", "Russian"]
#     },
#       "Argentina": {
#         "names": [
#             "Carlos", "Juan", "Ana", "Maria", "Pedro", "Luis", "Sofia", "Javier", "Monica", "Pablo",
#             "Jorge", "Luciana", "Ricardo", "Gabriela", "Roberto", "Laura", "Patricia", "Fernando",
#             "Raul", "Andres", "Carmen", "Silvia", "Antonio", "Veronica", "Marta", "Belen", "Diego",
#             "Esteban", "Mariana", "Miguel", "Natalia", "Ezequiel", "Leandro", "Roxana", "Horacio",
#             "Fabian", "Santiago", "Paola", "Martín", "Fabiana", "Oscar", "Claudia", "Alfredo",
#             "Cristina", "Alicia", "Emilia", "Ignacio", "Daniela", "Lucas", "Viviana", "Agustin",
#             "Marcos", "Gustavo", "Liliana", "Sabrina", "Antonio", "Rosana", "Vera", "Victoria",
#             "Martín", "Guadalupe", "Elena", "Ramiro", "Ricardo", "Lorena", "Emiliano", "Alina",
#             "Estefania", "María José", "Martín", "Victoria", "Cecilia", "Juliana", "Celeste",
#             "Valeria", "Eduardo", "Luisana", "Maximiliano", "Karina", "Eduarda", "Luis", "Walter",
#             "Leonor", "Leandro", "Renato", "Nora", "Lucas", "Jessica", "Horacio", "Valeria",
#             "Patricia", "Daniel", "Gustavo", "Santiago", "Liliana", "Luis", "Leonardo", "Miriam",
#             "Oscar", "Carlos", "Luis", "Fernando", "Ricardo"
#         ],
#         "cities": ["Buenos Aires", "Cordoba", "Rosario", "Mendoza", "La Plata"],
#         "ethnic_groups": ["White", "Mestizo", "Indigenous", "African", "Arab"]
#     },
#     "France": {
#         "names": [
#             "Pierre", "Marie", "Jean", "Luc", "Sophie", "Michel", "Isabelle", "Hélène", "François", "Claire",
#             "Jacques", "Nathalie", "Paul", "Élise", "Bernard", "Catherine", "David", "Monique", "Robert",
#             "Chantal", "Bernadette", "Jacqueline", "André", "Gérard", "Yvonne", "Julien", "Michel",
#             "Hugo", "Jean-Paul", "Claudine", "Thierry", "Valérie", "Fabienne", "Sylvie", "Dominique",
#             "Stéphane", "Aline", "Céline", "Philippe", "Charlotte", "Lucie", "Jacques", "Patrick",
#             "Renaud", "Martine", "Vincent", "Mélanie", "Caroline", "Pierre-Louis", "Frédéric", "Denise",
#             "Clément", "Maud", "Thierry", "Béatrice", "Sandrine", "Michel", "Isabelle", "Jean-Pierre",
#             "Charlotte", "Marianne", "David", "Corinne", "Franck", "Arnaud", "Dominique", "Michel",
#             "Nathalie", "Alain", "Géraldine", "Jean-Michel", "Pierre", "Marc", "Thierry", "Nadine",
#             "Jacqueline", "Catherine", "Philippe", "Dominique", "Jean", "Bernard", "Michel", "Hélène",
#             "Éric", "Ludivine", "Jean-François", "Régis", "Pauline", "Sylvie", "Michel", "Antoine", "Bernadette"
#         ],
#         "cities": ["Paris", "Marseille", "Lyon", "Toulouse", "Nice"],
#         "ethnic_groups": ["French", "Berber", "Arab", "African", "Asian"]
#     },
#     "Italy": {
#         "names": [
#             "Giuseppe", "Giulia", "Luca", "Maria", "Marco", "Francesco", "Laura", "Matteo", "Anna",
#             "Alessandro", "Simona", "Giovanni", "Elena", "Antonio", "Rita", "Carla", "Paolo", "Paola",
#             "Andrea", "Chiara", "Luigi", "Giovanna", "Alessandra", "Francesca", "Michele", "Giorgio",
#             "Valentina", "Stefano", "Antonio", "Claudia", "Filippo", "Federica", "Daniele", "Ilaria",
#             "Mario", "Barbara", "Marco", "Federico", "Sonia", "Gabriele", "Lucia", "Valerio",
#             "Tiziana", "Vincenzo", "Antonio", "Renato", "Paola", "Vittoria", "Giovanni", "Lucrezia",
#             "Elisabetta", "Silvia", "Caterina", "Laura", "Luigi", "Alberto", "Cristina", "Lorenzo",
#             "Stefania", "Roberta", "Giuseppe", "Raffaella", "Antonio", "Maria", "Matteo", "Francesca",
#             "Valentina", "Luca", "Maria Teresa", "Gianluca", "Michele", "Carlo", "Silvia", "Paolo",
#             "Luca", "Martina", "Alessandra", "Andrea", "Claudio", "Simona", "Adriana", "Stefano",
#             "Caterina", "Vittoria", "Tiziana", "Paolo", "Carlo", "Giorgio", "Elisabetta", "Alessandra"
#         ],
#         "cities": ["Rome", "Milan", "Naples", "Turin", "Florence"],
#         "ethnic_groups": ["Italian", "Sardinian", "Albanian", "Romanian", "North African"]
#     },
#     "Japan": {
#         "names": [
#             "Hiroshi", "Yuki", "Aiko", "Taro", "Keiko", "Haruki", "Yuki", "Sakura", "Akira", "Naomi",
#             "Ryo", "Hina", "Kaito", "Yui", "Daisuke", "Rika", "Ryu", "Mai", "Takahiro", "Ayaka",
#             "Kenji", "Miku", "Shota", "Saki", "Yusuke", "Megumi", "Takumi", "Satoru", "Ai", "Mitsuki",
#             "Rika", "Ren", "Keisuke", "Ami", "Sho", "Saki", "Yuji", "Tomoko", "Yuto", "Hana", "Natsuki",
#             "Issei", "Misaki", "Kenta", "Riko", "Kazuya", "Ayumi", "Haruto", "Yusuke", "Miyu", "Keiko",
#             "Haruki", "Mai", "Kaito", "Chihiro", "Shunya", "Miku", "Rie", "Kou", "Mei", "Shin", "Yumiko",
#             "Natsumi", "Satoru", "Aya", "Yukio", "Nanami", "Fumiko", "Mio", "Eri", "Takaya", "Ayaka",
#             "Hiroki", "Sora", "Risa", "Shu", "Naoko", "Chiyo", "Seiji", "Hiroshi", "Rika", "Kazuya"
#         ],
#         "cities": ["Tokyo", "Osaka", "Kyoto", "Sapporo", "Nagoya"],
#         "ethnic_groups": ["Japanese", "Ryukyuans", "Ainu", "Korean", "Chinese"]
#     },
#      "South Korea": {
#         "names": [
#             "Jin", "Min", "Seul", "Hana", "Jiwon", "Jiho", "Nari", "Yuna", "Jiwon", "Seojin",
#             "Minji", "Hyejin", "Kihee", "Sujin", "Hajin", "Soojin", "Sumin", "Haeun", "Naeun",
#             "Yujin", "Eunji", "Seoyoung", "Jisoo", "Jiwon", "Seungah", "Jiwon", "Minseok",
#             "Bomi", "Eunjin", "Haeun", "Jiyoung", "Minsun", "Seoeun", "Minseo", "Jiwon",
#             "Jieun", "Eunseo", "Yura", "Nuri", "Siyoung", "Nari", "Heejae", "Haemin", "Yuri",
#             "Jiwon", "Younghee", "Seojin", "Minseok", "Jiwon", "Sungho", "Seokmin", "Seojin",
#             "Jaejoong", "Jinwoo", "Doyeon", "Jihoon", "Kangmin", "Heejin", "Jiwon", "Jinsol",
#             "Seonghyun", "Jiho", "Yunho", "Hyewon", "Mina", "Kyungsoo", "Jiwon", "Sujin",
#             "Seungmin", "Yeji", "Eunyoung", "Jiwon", "Jeonghan", "Soobin", "Yunji", "Sungmin",
#             "Heeji", "Jiwon", "Jimin", "Mingi", "Doyoung", "Gaeun", "Minjeong", "Soojin",
#             "Seungwoo", "Dohyun", "Eunhee", "Soojin", "Nayeon", "Hyunjoon", "Minjae", "Heewon"
#         ],
#         "cities": ["Seoul", "Busan", "Incheon", "Daegu", "Gwangju"],
#         "ethnic_groups": ["Korean", "Chinese", "Japanese", "Other"]
#     },
#     "Canada": {
#         "names": [
#             "James", "Emily", "Oliver", "Liam", "Charlotte", "Ethan", "Amelia", "Aiden", "Olivia",
#             "Lucas", "Ella", "Benjamin", "Grace", "Matthew", "Sophia", "Jack", "Chloe", "William",
#             "Zoe", "Mason", "Madeline", "Noah", "Avery", "Ryan", "Sophie", "Ethan", "Mia", "Jacob",
#             "Hannah", "Samuel", "Isabella", "Daniel", "Emma", "Nathan", "Victoria", "Lily", "Carter",
#             "Dylan", "Harper", "Cameron", "Scarlett", "Lucas", "Peyton", "Austin", "Lila", "Landon",
#             "Madison", "Alexander", "Leah", "Miles", "Chase", "Parker", "Aiden", "Lily", "Finn",
#             "Eva", "Eva", "Jack", "Charlotte", "Brody", "Owen", "Tessa", "Isla", "Henry", "Maya",
#             "Benjamin", "Aiden", "Sophie", "Ella", "Zoe", "Madeline", "Joseph", "Emma", "Nolan",
#             "Isabella", "Noah", "Harper", "Evelyn", "Evan", "Liam", "Kaitlyn", "Samantha", "Violet"
#         ],
#         "cities": ["Toronto", "Vancouver", "Montreal", "Ottawa", "Calgary"],
#         "ethnic_groups": ["Canadian", "English", "French", "Indigenous", "Other"]
#     },
#     "Mexico": {
#         "names": [
#             "Carlos", "Luis", "Maria", "Jose", "Pedro", "Ana", "Juan", "Rosa", "Francisco", "Patricia",
#             "Antonio", "Luisa", "Miguel", "Sofia", "Raul", "Sandra", "Javier", "Gabriela", "Ricardo",
#             "Luis", "Raquel", "Emilio", "Martin", "Oscar", "Hector", "Teresa", "Antonio", "Juanita",
#             "Maribel", "Francisco", "Claudia", "Jorge", "Santiago", "Alfonso", "Monica", "Cristina",
#             "Elena", "Arturo", "Victor", "Veronica", "Josefina", "Alma", "Gerardo", "Ramiro", "Ricardo",
#             "Julieta", "Carlos", "Rosa", "Hilda", "Tomas", "Ramon", "Adriana", "Felipe", "Angelica",
#             "Rodolfo", "David", "Santiago", "Miguel", "Enrique", "Guadalupe", "Miguel Angel",
#             "Liliana", "Guadalupe", "Bernardo", "Luis Fernando", "Teresa", "Gilberto", "Felix",
#             "Victor", "Leticia", "Julian", "Raul", "Oscar", "Paola", "Carolina", "Jaime", "Berenice",
#             "Victor", "Nancy", "Carlos", "Marco", "Daniela", "Esther", "Enrique", "Carlos", "Lucia"
#         ],
#         "cities": ["Mexico City", "Guadalajara", "Monterrey", "Cancun", "Tijuana"],
#         "ethnic_groups": ["Mestizo", "Indigenous", "White", "Black", "Asian"]
#     },
#     "Russia": {
#         "names": [
#             "Ivan", "Olga", "Alexei", "Maria", "Nikolai", "Dmitri", "Tatiana", "Vladimir", "Anastasia",
#             "Vera", "Sergey", "Ekaterina", "Aleksei", "Irina", "Pavel", "Svetlana", "Andrei", "Olga",
#             "Roman", "Marina", "Oleg", "Elena", "Maxim", "Valentina", "Yulia", "Leonid", "Tatyana",
#             "Viktor", "Vera", "Kirill", "Ludmila", "Alexandra", "Vsevolod", "Daria", "Denis", "Larisa",
#             "Arkady", "Nina", "Anastasia", "Yegor", "Irina", "Mikhail", "Olga", "Victor", "Galina",
#             "Timofey", "Sofia", "Alexander", "Yana", "Natalia", "Evgeny", "Maria", "Aleksey", "Nikolay",
#             "Yekaterina", "Dmitriy", "Boris", "Yelena", "Igor", "Tatiana", "Elizaveta", "Anton",
#             "Viktoria", "Oksana", "Vadim", "Konstantin", "Tatyana", "Ekaterina", "Inna", "Raisa",
#             "Gennady", "Vladimir", "Sergei", "Valery", "Evgeniya", "Anatoly", "Anna", "Alexei", "Igor"
#         ],
#         "cities": ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Nizhny Novgorod"],
#         "ethnic_groups": ["Russian", "Tatar", "Ukrainian", "Bashkir", "Chuvash"]
#     },
#    "Australia": {
#         "names": [
#             "Jack", "Emily", "Oliver", "Charlotte", "Mia", "Liam", "Ava", "Jackson", "Sophia",
#             "Noah", "Amelia", "Lucas", "Isabella", "Mason", "Lily", "Ethan", "Chloe", "Aiden",
#             "Grace", "Ben", "Megan", "Zoe", "Logan", "Ella", "Ryan", "Ruby", "William", "Mia",
#             "Madeline", "Isaac", "Charlotte", "Jacob", "Hannah", "Lucas", "Peyton", "Charlotte",
#             "Oliver", "Chloe", "Ben", "Zoe", "Evan", "Sophie", "Grace", "Oliver", "Ella", "Henry",
#             "Maya", "Evan", "Harper", "Liam", "Victoria", "David", "Carter", "Megan", "Sophie",
#             "Emma", "Oliver", "Charlotte", "Ethan", "William", "James", "Amelia", "Jack", "Olivia",
#             "Jacob", "Emily", "Chloe", "Charlotte", "Henry", "Zoe", "Madison", "Ryan", "Ella",
#             "Sophia", "Jack", "Lily", "Sophie", "Megan", "Benjamin", "Sophia", "Ella", "Oliver",
#             "Aiden", "Zoe", "Chloe", "Mia", "Ella", "Charlotte", "Harper", "Ryan", "Zoe", "Liam"
#         ],
#         "cities": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"],
#         "ethnic_groups": ["Australian", "English", "Irish", "Scottish", "Indigenous"]
#     },
#     "Egypt": {
#         "names": [
#             "Ahmed", "Fatima", "Mona", "Omar", "Yasmin", "Mohamed", "Hassan", "Layla", "Ali",
#             "Zainab", "Mahmoud", "Nadia", "Amina", "Mustafa", "Salma", "Khaled", "Mariam",
#             "Youssef", "Heba", "Tamer", "Sara", "Khalil", "Reem", "Ibrahim", "Farida", "Omar",
#             "Dalia", "Amr", "Hana", "Rania", "Yasmine", "Fayza", "Ahmed", "Mohamed", "Fatma",
#             "Alaa", "Eman", "Ahmed", "Rana", "Mona", "Mohamed", "Sami", "Rania", "Maha",
#             "Nadia", "Ahmed", "Mariam", "Nour", "Amina", "Mahmoud", "Amira", "Mohamed",
#             "Fady", "Dina", "Ibrahim", "Salma", "Omar", "Laila", "Fahim", "Yousra", "Khaled",
#             "Hala", "Osman", "Maha", "Lina", "Sherif", "Mohamed", "Mai", "Hossam", "Sama",
#             "Abdallah", "Fawzi", "Sherif", "Yasmin", "Hossam", "Fayza", "Ali", "Sami",
#             "Maha", "Khaled", "Alaa", "Amira", "Mohamed", "Ramy", "Mira", "Ali", "Maha"
#         ],
#         "cities": ["Cairo", "Alexandria", "Giza", "Luxor", "Aswan"],
#         "ethnic_groups": ["Egyptian", "Berber", "Nubian", "Bedouin", "Other"]
#     },
# }

# # Dân tộc tương ứng với từng quốc gia
# ethnic_groups = {
#     "Vietnam": ["Kinh", "Tay", "Thai", "Muong", "H'mong"],
#     "China": ["Han", "Tibetan", "Uighur", "Zhuang", "Mongol"],
#     "United States of America": ["White", "Black or African American", "Hispanic or Latino", "Asian", "Native American"],
#     "Brazil": ["White", "Pardo", "Black", "Asian", "Indigenous"],
#     "India": ["Hindu", "Muslim", "Sikh", "Christian", "Other"],
#     "Germany": ["German", "Turkish", "Kurdish", "Polish", "Russian"],
#     "Argentina": ["White", "Mestizo", "Indigenous", "African", "Arab"],
#     "France": ["French", "Berber", "Arab", "African", "Asian"],
#     "Italy": ["Italian", "Sardinian", "Albanian", "Romanian", "North African"],
#     "Japan": ["Japanese", "Ryukyuans", "Ainu", "Korean", "Chinese"],
#     "South Korea": ["Korean", "Chinese", "Japanese", "Other"],
#     "Canada": ["Canadian", "English", "French", "Indigenous", "Other"],
#     "Mexico": ["Mestizo", "Indigenous", "White", "Black", "Asian"],
#     "Russia": ["Russian", "Tatar", "Ukrainian", "Bashkir", "Chuvash"],
#     "Australia": ["Australian", "English", "Irish", "Scottish", "Indigenous"],
#     "Egypt": ["Egyptian", "Berber", "Nubian", "Bedouin", "Other"]
# }

# # Hàm lấy dân tộc ngẫu nhiên cho mỗi quốc gia
# def get_random_ethnic_group(nationality):
#     if nationality in ethnic_groups:
#         return random.choice(ethnic_groups[nationality])
#     return None

# # Hàm tạo dữ liệu ngẫu nhiên với phân phối ngẫu nhiên có trọng số
# def generate_random_data(num_rows, start_id=307):
#     data = []
#     countries = list(country_data.keys())
#     weights = [
#         0.05,   # Vietnam
#         0.15,   # China
#         0.30,   # United States of America (trên 20%)
#         0.05,   # Brazil
#         0.2,   # India
#         0.05,   # Germany
#         0.05,   # Argentina
#         0.05,   # France
#         0.05,   # Italy
#         0.05,   # Japan
#         0.05,   # South Korea
#         0.05,   # Canada
#         0.05,   # Mexico
#         0.05,   # Russia
#         0.05,   # Australia
#         0.05,   # Egypt
#     ]

#     for i in range(num_rows):
#         nationality = random.choices(countries, weights=weights)[0]
#         name = random.choice(country_data[nationality]["names"])
#         city = random.choice(country_data[nationality]["cities"])
#         ethnic_group = get_random_ethnic_group(nationality)

#         data.append({
#             "id": start_id + i,
#             "name": name,
#             "nationality": nationality,
#             "city": city,
#             "latitude": round(random.uniform(-90, 90), 2),
#             "longitude": round(random.uniform(-180, 180), 2),
#             "gender": random.choice(["M", "F"]),
#             "ethnic.group": ethnic_group,
#             "age": random.randint(18, 30),
#             "english.grade": round(random.uniform(1.0, 5.0), 1),
#             "math.grade": round(random.uniform(1.0, 5.0), 1),
#             "sciences.grade": round(random.uniform(1.0, 5.0), 1),
#             "language.grade": round(random.uniform(1.0, 5.0), 1),
#             "portfolio.rating": random.randint(1, 5),
#             "coverletter.rating": random.randint(1, 5),
#             "refletter.rating": random.randint(1, 5)
#         })

#     return data

# # Tạo dữ liệu và lưu vào file CSV
# num_new_rows = 2000
# new_data = generate_random_data(num_new_rows, start_id=307)

# df_new = pd.DataFrame(new_data)
# file_path = "data/demo.csv"
# df_new.to_csv(file_path, index=False)

# print(f"Đã tạo và lưu {num_new_rows} dòng dữ liệu vào file: {file_path}")


# import pandas as pd

# # Hàm đọc dữ liệu từ file CSV và loại bỏ các dòng có tên trùng
# def remove_duplicate_names(csv_file):
#     # Đọc dữ liệu từ file CSV
#     df = pd.read_csv(csv_file)

#     # Loại bỏ các dòng có tên trùng (giữ lại dòng đầu tiên)
#     df_cleaned = df.drop_duplicates(subset=["name"], keep="first")

#     # Trả về dữ liệu đã loại bỏ tên trùng
#     return df_cleaned

# # Ví dụ sử dụng hàm
# csv_file = "data/student-dataset.csv"  # Đường dẫn đến file CSV của bạn
# cleaned_data = remove_duplicate_names(csv_file)

# # In ra một số dòng đầu của dữ liệu đã được làm sạch
# print(cleaned_data.head())

# # Nếu muốn lưu lại file đã làm sạch
# cleaned_data.to_csv("data/student-dataset.csv", index=False)
import pandas as pd
import numpy as np
import random

# Danh sách dân tộc theo quốc gia
ethnic_groups_by_country = {
    "Vietnam": ["Kinh", "Tay", "Thai", "Muong", "H'mong"],
    "China": ["Han", "Tibetan", "Uighur", "Zhuang", "Mongol"],
    "United States of America": ["White", "Black or African American", "Hispanic or Latino", "Asian", "Native American"],
    "Brazil": ["White", "Pardo", "Black", "Asian", "Indigenous"],
    "India": ["Hindu", "Muslim", "Sikh", "Christian", "Other"],
    "Germany": ["German", "Turkish", "Kurdish", "Polish", "Russian"],
    "Argentina": ["White", "Mestizo", "Indigenous", "African", "Arab"],
    "France": ["French", "Berber", "Arab", "African", "Asian"],
    "Italy": ["Italian", "Sardinian", "Albanian", "Romanian", "North African"],
    "Japan": ["Japanese", "Ryukyuans", "Ainu", "Korean", "Chinese"],
    "South Korea": ["Korean", "Chinese", "Japanese", "Other"],
    "Canada": ["Canadian", "English", "French", "Indigenous", "Other"],
    "Mexico": ["Mestizo", "Indigenous", "White", "Black", "Asian"],
    "Russia": ["Russian", "Tatar", "Ukrainian", "Bashkir", "Chuvash"],
    "Australia": ["Australian", "English", "Irish", "Scottish", "Indigenous"],
    "Egypt": ["Egyptian", "Berber", "Nubian", "Bedouin", "Other"]
}

# Hàm thêm dân tộc ngẫu nhiên vào ô trống


def add_random_ethnic_group(input_file='data/demo.csv', output_file='data/demo.csv'):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(input_file)

    # Kiểm tra xem cột 'ethnic_group' có tồn tại hay không
    if 'ethnic.group' not in df.columns:
        print("Cột 'ethnic.group' không tồn tại trong file.")
        return

    # Kiểm tra xem cột 'nationality' có tồn tại hay không
    if 'nationality' not in df.columns:
        print("Cột 'nationality' không tồn tại trong file.")
        return

    # Thay thế giá trị trống trong cột 'ethnic.group' bằng dân tộc ngẫu nhiên từ quốc gia
    def random_ethnic_group(row):
        if pd.isna(row['ethnic.group']) or row['ethnic.group'] == 'NAN':
            nationality = row['nationality']
            if nationality in ethnic_groups_by_country:
                # Lấy danh sách dân tộc theo quốc gia và chọn ngẫu nhiên
                return random.choice(ethnic_groups_by_country[nationality])
            else:
                return 'NAN'  # Nếu quốc gia không có trong danh sách, gán 'NAN'
        else:
            return row['ethnic.group']

    # Áp dụng hàm random_ethnic.group cho từng dòng dữ liệu
    df['ethnic.group'] = df.apply(random_ethnic_group, axis=1)

    # Lưu DataFrame vào file CSV
    df.to_csv(output_file, index=False)
    print(f"Dữ liệu đã được lưu vào {output_file}.")


# Gọi hàm
add_random_ethnic_group()
