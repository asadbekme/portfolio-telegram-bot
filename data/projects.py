from telebot import types

PROJECTS = [
    {
        "id": "alif_market",
        "title": "Alif Market Group",
        "description": "Zamonaviy bizneslar uchun raqamli yechimlarni yaratish va amalga oshirishga ixtisoslashgan investitsiya kompaniyasi.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1768809820766-q3szpk.png",
        "tech": ["React", "Next.js", "Tailwind CSS", "TypeScript", "Tanstack Query", "Headless UI"],
        "live_url": "https://aetestdomain.com",
        "github_url": "https://github.com/asadbekme"
    },
    {
        "id": "dieselly",
        "title": "Dieselly AI",
        "description": "Tejamkorlikni oshirish, haydashni optimallashtirish - avtopark va mustaqil avtomobillar uchun mo‘ljallangan yoqilg‘i kartasi muqobili.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1768835532225-bppveq.png",
        "tech": ["React", "Next JS", "Tailwind CSS", "Shadcn UI", "Rest API", "Here Map", "TypeScript", "Zustand"],
        "live_url": "https://dieselly.ai",
        "github_url": "https://github.com/asadbekme"
    },
    {
        "id": "doner_food",
        "title": "Doner Food",
        "description": "Biz tezkor xizmat, mazali taom va do'stona muhitni taklif qilamiz. Bugun buyurtma bering va ta'mdan bahramand bo'ling!",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1768835164338-nwpbeu.png",
        "tech": ["React", "Supabase", "TypeScript", "Shadcn UI", "Tailwind CSS", "PostgreSQL"],
        "live_url": "https://www.donerfood.uz",
        "github_url": "https://github.com/asadbekme/doner-food"
    },
    {
        "id": "task_manager",
        "title": "Vazifalarni boshqarish ilovasi",
        "description": "Aynan Kanban uslubidagi tortish va tashlash, vazifa ko'rinishlari va admin nazorati bilan zamonaviy vazifalarni boshqarish ilovasi.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1768816741288-gfzhwi.webp",
        "tech": ["Next.js", "Shadcn UI", "Tailwind CSS", "TypeScript", "jsonstorage.net", "Tanstack Query"],
        "live_url": "https://task-management-app-by-asadbekjs.vercel.app",
        "github_url": "https://github.com/asadbekme/task-management-app"
    },
    {
        "id": "education_crm",
        "title": "Ta'lim CRM tizimi",
        "description": "Foydalanuvchi autentifikatsiyasi, rolga asoslangan kirish va moslashuvchan dizayn bilan ta'minlangan ta'lim muassasalari uchun keng qamrovli CRM tizimi.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1768834310463-spj4cp.jpg",
        "tech": ["React", "Next.js", "Shadcn UI", "Tailwind CSS", "Typescript", "Recharts"],
        "live_url": "https://education-crm-flame.vercel.app",
        "github_url": "https://github.com/asadbekme/education-crm"
    },
    {
        "id": "glasses_shop",
        "title": "Ko'zoynak do'koni veb-sayti",
        "description": "Zamonaviy elektron kommeritsiya uchun elegant va moslashuvchan veb-sayt.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1768834630575-c5cwgu.png",
        "tech": ["HTML", "SASS", "JavaScript"],
        "live_url": "https://glasses-website-design.netlify.app",
        "github_url": "https://github.com/asadbekme/glasses-website-design"
    },
    {
        "id": "learnify",
        "title": "Learnify",
        "description": "O‘quv markazlari uchun marketing veb-saytlari va sahifalar tarkibini admin panelidan to‘liq boshqarish mumkin.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1772616881161-9khjhk.png",
        "tech": ["React", "Tailwind CSS", "Supabase", "Shadcn UI", "TypeScript", "Tanstack Query"],
        "live_url": "https://learnify-lc.vercel.app",
        "github_url": "https://github.com/asadbekme"
    },
    {
        "id": "inkwell",
        "title": "Inkwell",
        "description": "Inkwell - bu Medium’dan ilhomlangan, har qanday mavzuda hikoyalarni o‘qish va yozish uchun mo‘ljallangan zamonaviy, to‘liq stekli blog yuritish platformasi. Samaradorlik va SEOni hisobga olgan holda ishlabcfgan bo‘lib, u sahifalarni tez yuklash va optimal topiluvchanlikni ta’minlash uchun server tomonidagi renderlash (SSR) tizimidan foydalanadi.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1777057456165-cculfi.png",
        "tech": ["React", "Vite", "TanStack Start", "TanStack Router", "Tailwind CSS", "Supabase", "Shadcn UI"],
        "live_url": "https://inkwell-app.asadbekme2002.workers.dev/",
        "github_url": "https://github.com/asadbekme"
    }
]

def get_projects_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for i, project in enumerate(PROJECTS):
        keyboard.add(types.InlineKeyboardButton(f"💻 {project['title']}", callback_data=f"proj_{i}"))
    return keyboard
