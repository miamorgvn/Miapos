// ============================================================
//  miamotion app - C++ launcher
// ============================================================
//  Launcher native: cek environment -> auto-update -> jalankan
//  server Python. Dipakai biar app bisa dibuka seperti program
//  biasa (./launch di PC/Termux, launch.exe di Windows).
//
//  Build:
//    Linux / Termux : g++ -O2 -std=c++17 -o launch launcher.cpp
//    Windows (MinGW): g++ -O2 -std=c++17 -o launch.exe launcher.cpp
//
//  Jalankan dari folder utama project (yang berisi server/):
//    ./launch           -> update + start server
//    ./launch --check   -> cek environment saja lalu keluar
// ============================================================

#include <cstdio>
#include <fstream>
#include <iostream>
#include <string>

#ifdef _WIN32
  #include <windows.h>
  static const char* PY = "python";
  static const char* QUIET = " > NUL 2>&1";
#else
  static const char* PY = "python3";
  static const char* QUIET = " >/dev/null 2>&1";
#endif

static bool fileExists(const std::string& path) {
    std::ifstream f(path);
    return f.good();
}

static int run(const std::string& cmd) {
    return std::system(cmd.c_str());
}

int main(int argc, char** argv) {
#ifdef _WIN32
    SetConsoleOutputCP(CP_UTF8);
#endif
    bool checkOnly = false;
    for (int i = 1; i < argc; ++i) {
        if (std::string(argv[i]) == "--check") checkOnly = true;
    }

    std::cout
        << "\n"
        << "  ==============================\n"
        << "   miamotion app  -  launcher\n"
        << "  ==============================\n\n";

    // Harus dijalankan dari root project
    if (!fileExists("server/app.py")) {
        std::cout << "  [x] server/app.py tidak ditemukan.\n"
                  << "      Jalankan launcher dari folder utama project!\n\n";
        return 1;
    }

    // Python tersedia?
    int rc = run(std::string(PY) + " --version" + QUIET);
    if (rc != 0) {
        std::cout << "  [x] Python tidak ditemukan!\n"
                  << "      Termux : pkg install python\n"
                  << "      PC     : install dari https://python.org\n"
                  << "      Windows: install dari https://python.org (centang 'Add to PATH')\n\n";
        return 1;
    }

    if (checkOnly) {
        std::cout << "  [ok] environment siap (python ditemukan)\n\n";
        return 0;
    }

    // [1/2] Auto-update dari GitHub
    std::cout << "  [1/2] Cek update dari GitHub...\n";
    run(std::string(PY) + " server/updater.py --once");

    // [2/2] Start server (blocking sampai Ctrl+C)
    std::cout << "  [2/2] Menyalakan server...\n\n";
    int code = run(std::string(PY) + " server/app.py");
    return code;
}
