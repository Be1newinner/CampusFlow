# 🎓 CampusFlow – Education CRM Backend

CampusFlow is an **open-source CRM platform** designed for **education institutes**, **coaching centers**, and **training academies** to streamline operations such as student management, course scheduling, attendance, fee tracking, lead management, and more.

---

## 🚀 Project Status

CampusFlow is currently in **active development** (MVP phase). This backend is being built using:

- ⚙️ FastAPI (Python 3.11+)
- 🗃️ PostgreSQL
- 🧠 SQLAlchemy (with Alembic)
- 🔐 JWT-based Auth
- 📦 Modular architecture
- 🐳 Docker-ready

---

## 👤 About Me

Hi, I'm **Vijay**, a Full Stack Developer and trainer at Asha Tech (Delhi), currently building **CampusFlow** to solve real-world problems faced by education institutes.

You can find me sharing development tutorials on my [YouTube Channel – Asaan Hai Coding](https://www.youtube.com/@asaan_hai_coding).

---

## 🧩 Planned Modules

| Module              | Description |
|---------------------|-------------|
| 🔐 Authentication    | JWT-based login for Admin, Staff, Students |
| 👨‍🏫 Staff Management | Add/edit staff, assign to courses, attendance |
| 🎓 Student Management| Profile, course enrollment, fee tracking |
| 📚 Courses & Batches | Manage courses, schedule batches |
| 📅 Attendance        | Track attendance per class/batch |
| 💰 Fee Management    | Payment records, reminders, receipts |
| 🎯 Lead CRM          | Track leads, follow-ups, conversion |
| 📩 Notifications     | Email/SMS alerts for reminders, updates |
| 🧾 Reports & Stats   | Attendance %, fee dues, revenue analytics |
| 📁 Documents         | Upload student/staff documents |

---

## 📦 Tech Stack

- **Backend Framework:** FastAPI
- **ORM:** SQLAlchemy + Alembic
- **Database:** PostgreSQL
- **Auth:** JWT + OAuth (upcoming)
- **Containerization:** Docker
- **Deployment-ready:** Yes (VPS/Nginx/Gunicorn setup planned)

---

## 👐 Open Source & Contributions

> 🎉 This is an **open-source project** — feel free to:
- Fork it 🍴
- Improve it 🔧
- Suggest features 💡
- Fix bugs 🐛
- Add docs 📝
- Or just star ⭐ the repo to support!

**Contributions are welcome via Pull Requests!**

## 📁 Folder Structure (Planned)

```bash
campusflow/
│
├── app/
│   ├── features/
│   │   ├── auth/
│   │   ├── students/
│   │   ├── staff/
│   │   ├── courses/
│   │   ├── fees/
│   │   ├── leads/
│   │   ├── attendance/
│   │   └── notifications/
│   │
│   ├── core/             # Settings, error handlers, app config
│   ├── db/               # DB session, Alembic, base metadata
│   ├── utils/            # Shared utils like email, password hashing
│   └── main.py           # FastAPI entry point
```

## 📌 Roadmap (MVP)

* [x] Project scaffolding + Docker
* [ ] Auth (JWT, roles)
* [ ] Students + Staff APIs
* [ ] Courses + Batches
* [ ] Fee Tracking
* [ ] Leads CRM
* [ ] Email reminders
* [ ] Admin dashboard (planned with Next.js)

---

## 📜 License

This project is licensed under the **MIT License**.
You're free to reuse, modify, and build upon it — just give credit!

---

## 📬 Contact

* 📧 Email: [be1newinner@gmail.com](mailto:asaanhaicoding@gmail.com)
* 🌐 YouTube: [@asaan\_hai\_coding](https://www.youtube.com/@asaan_hai_coding)