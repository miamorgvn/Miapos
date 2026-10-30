// ============================================================
//  MIAPOS NATIVE ANALYTICS ENGINE — C++17 (tanpa dependensi)
// ============================================================
//  Input  (stdin) : per baris "<unix_ts> <amount>" (omzet harian,
//                   urut naik). Baris kosong diabaikan.
//  Output (stdout): total|days|avg|growth_pct|movavg7|best_ts|best_amount|forecast|trend
//
//  Dipanggil oleh server Python (main.py) lewat subprocess.
//  Kalau binary ini tidak ada, Python otomatis pakai mode
//  fallback murni Python — aplikasi tetap jalan normal.
// ============================================================

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <iostream>
#include <algorithm>

struct Day {
    long long ts;
    double amount;
};

static double avg_of(const std::vector<Day>& d, size_t from, size_t to) {
    // rata-rata rentang [from, to) — aman untuk rentang kosong
    if (from >= to) return 0.0;
    double s = 0.0;
    for (size_t i = from; i < to; i++) s += d[i].amount;
    return s / static_cast<double>(to - from);
}

int main() {
    std::vector<Day> days;
    days.reserve(64);
    long long ts;
    double amt;
    while (std::cin >> ts >> amt) {
        if (ts >= 0) days.push_back({ts, amt});
    }

    const size_t n = days.size();

    // ---- kasus kosong ----
    if (n == 0) {
        std::printf("0|0|0|0|0|0|0|0|KOSONG\n");
        return 0;
    }

    // ---- total & rata-rata ----
    double total = 0.0;
    for (const auto& d : days) total += d.amount;
    const double avg = total / static_cast<double>(n);

    // ---- growth: bandingkan 7 hari terakhir vs 7 hari sebelumnya ----
    const size_t last7_from = n > 7 ? n - 7 : 0;
    const size_t last7_to   = n;
    const size_t prev7_to   = last7_from;
    const size_t prev7_from = prev7_to > 7 ? prev7_to - 7 : 0;
    const double last7_avg = avg_of(days, last7_from, last7_to);
    const double prev7_avg = (n > 7) ? avg_of(days, prev7_from, prev7_to) : 0.0;
    double growth = 0.0;
    if (prev7_avg > 0.000001) growth = ((last7_avg - prev7_avg) / prev7_avg) * 100.0;
    else if (last7_avg > 0.000001 && n > 7) growth = 100.0;

    // ---- hari terbaik ----
    const Day* best = &days[0];
    for (const auto& d : days) if (d.amount > best->amount) best = &d;

    // ---- prediksi besok: weighted average (70% minggu ini + 30% keseluruhan) ----
    const double forecast = std::max(0.0, 0.7 * last7_avg + 0.3 * avg);

    // ---- label tren ----
    const char* trend = "STABIL";
    if (growth > 5.0) trend = "NAIK";
    else if (growth < -5.0) trend = "TURUN";

    std::printf("%.2f|%zu|%.2f|%.2f|%.2f|%lld|%.2f|%.2f|%s\n",
                total, n, avg, growth, last7_avg,
                best->ts, best->amount, forecast, trend);
    return 0;
}
