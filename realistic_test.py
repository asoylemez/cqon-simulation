"""
CQON Model - Gerçek Koşullarda Test
Doğal sistemlere uygun parametrelerle test
"""

import numpy as np
import matplotlib.pyplot as plt
from cqon_model import CQONSimulation

# TÜRKÇE KARAKTER DÜZELTMESİ - Bu satırları ekleyin
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


def realistic_parameter_sweep():
    """Gerçekçi parametre taraması"""
    print("🔬 GERÇEK KOŞULLARDA CQON TESTİ")
    print("=" * 60)

    # Gerçekçi senaryolar - doğal sistemlere benzer
    scenarios = [
        {
            "name": "OPTIMUM KUANTUM ORTAM",
            "desc": "Dusuk sicaklik, yuksek koherans - laboratuvar kosullari",
            "alpha": 0.45, "gamma": 0.05, "T": 0.08, "K0": 1.1,
            "grid_size": 12, "total_time": 80, "dt": 0.2
        },
        {
            "name": "ERKEN DUNYA BENZERI",  # Türkçe karakter kaldırıldı
            "desc": "Orta seviye gurultu - prebiyotik Dunya kosullari",
            "alpha": 0.35, "gamma": 0.07, "T": 0.15, "K0": 0.9,
            "grid_size": 12, "total_time": 100, "dt": 0.2
        },
        {
            "name": "OKYANUS DIPI KOSULLARI",
            "desc": "Yuksek basinc/kararlilik - hidrotermal bacalar",
            "alpha": 0.38, "gamma": 0.04, "T": 0.12, "K0": 1.0,
            "grid_size": 12, "total_time": 120, "dt": 0.2
        },
        {
            "name": "YUKSEK GURULTULU ORTAM",
            "desc": "Turbulansli ortam - nehir agizlari, gelgit bolgeleri",
            "alpha": 0.28, "gamma": 0.10, "T": 0.22, "K0": 0.8,
            "grid_size": 12, "total_time": 100, "dt": 0.2
        },
        {
            "name": "KRITIK ESIK TESTI",
            "desc": "Yasam esiginde - teorik minimum kosullar",
            "alpha": 0.32, "gamma": 0.08, "T": 0.18, "K0": 0.85,
            "grid_size": 12, "total_time": 150, "dt": 0.2
        }
    ]

    results = []

    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{i}. 📋 {scenario['name']}")
        print(f"   📝 {scenario['desc']}")
        print(f"   ⚙️  Parametreler: α={scenario['alpha']}, γ={scenario['gamma']}, "
              f"T={scenario['T']}, K₀={scenario['K0']}")

        try:
            sim = CQONSimulation(
                alpha=scenario['alpha'],
                gamma=scenario['gamma'],
                T=scenario['T'],
                K0=scenario['K0'],
                grid_size=scenario['grid_size'],
                total_time=scenario['total_time'],
                dt=scenario['dt']
            )

            # Detaylı sonuçlar için
            results_dict = sim.run(verbose=False)
            results_dict['scenario'] = scenario['name']
            results.append(results_dict)

            # Detaylı analiz
            print(f"   📊 SONUCLAR:")
            print(f"      • Ortalama koherans: {results_dict['avg_coherence']:.3f}")
            print(f"      • Koherans adalari: {results_dict['coherence_islands']}")
            print(f"      • Enerji: {results_dict['final_energy']:.1f}")
            print(f"      • Entropi: {results_dict['final_entropy']:.1f}")
            print(f"      • E-S Korelasyon: {results_dict['energy_entropy_correlation']:.3f}")
            print(f"      • Yasam-benzeri: {'EVET' if results_dict['life_like_organization'] else 'HAYIR'}")

            # Gelişmiş yaşam analizi
            life_status = analyze_life_likelihood(results_dict)
            print(f"      • 🎯 YASAM OLASILIGI: {life_status}")

        except Exception as e:
            print(f"   ❌ Hata: {e}")
            continue

    return results


def analyze_life_likelihood(results):
    """Yaşam olasılığını detaylı analiz et"""
    score = 0
    feedback = []

    # Koherans puanı
    if results['avg_coherence'] > 0.45:
        score += 3
        feedback.append("Yuksek koherans ✅")
    elif results['avg_coherence'] > 0.35:
        score += 2
        feedback.append("Orta koherans ⚠️")
    else:
        feedback.append("Dusuk koherans ❌")

    # Ada puanı
    if results['coherence_islands'] >= 3:
        score += 3
        feedback.append("Coklu kararli adalar ✅")
    elif results['coherence_islands'] >= 2:
        score += 2
        feedback.append("Kararli ada olusumu ⚠️")
    else:
        feedback.append("Yetersiz ada olusumu ❌")

    # Enerji-Entropi puanı
    corr = results['energy_entropy_correlation']
    if corr < -0.6:
        score += 3
        feedback.append("Guclu enerji-enformasyon donusumu ✅")
    elif corr < -0.4:
        score += 2
        feedback.append("Orta enerji-enformasyon donusumu ⚠️")
    else:
        feedback.append("Zayif enerji-enformasyon donusumu ❌")

    # Karar
    if score >= 7:
        return "YUKSEK - Guclu yasam-benzeri organizasyon 🎯"
    elif score >= 5:
        return "ORTA - Zayif yasam-benzeri organizasyon 📈"
    elif score >= 3:
        return "DUSUK - On-yasamsal organizasyon 📉"
    else:
        return "YOK - Kaotik durum ❌"


def plot_comprehensive_results(results):
    """Kapsamlı sonuç görselleştirmesi"""
    if not results:
        print("❌ Görselleştirme için sonuç yok!")
        return

    fig, axes = plt.subplots(2, 2, figsize=(15, 12))

    # 1. Senaryo karşılaştırması
    scenarios = [r['scenario'] for r in results]
    coherence = [r['avg_coherence'] for r in results]
    islands = [r['coherence_islands'] for r in results]

    x_pos = np.arange(len(scenarios))

    axes[0, 0].bar(x_pos - 0.2, coherence, 0.4, label='Ortalama Koherans', alpha=0.7, color='blue')
    axes[0, 0].bar(x_pos + 0.2, islands, 0.4, label='Koherans Adalari', alpha=0.7, color='green')
    axes[0, 0].set_xlabel('Senaryolar')
    axes[0, 0].set_ylabel('Degerler')
    axes[0, 0].set_title('CQON Senaryo Karsilastirmasi')
    axes[0, 0].set_xticks(x_pos)
    axes[0, 0].set_xticklabels([s[:15] + '...' for s in scenarios], rotation=45)
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # 2. Enerji-Entropi korelasyonu
    correlations = [r['energy_entropy_correlation'] for r in results]
    axes[0, 1].bar(range(len(scenarios)), correlations, color='purple', alpha=0.7)
    axes[0, 1].axhline(y=-0.4, color='red', linestyle='--', label='Kritik Esik')
    axes[0, 1].set_xlabel('Senaryolar')
    axes[0, 1].set_ylabel('Korelasyon Katsayisi')
    axes[0, 1].set_title('Enerji-Entropi Korelasyonu (CQON)')
    axes[0, 1].set_xticks(range(len(scenarios)))
    axes[0, 1].set_xticklabels([s[:15] + '...' for s in scenarios], rotation=45)
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)

    # 3. Zaman evrimi örneği (ilk senaryo)
    if results:
        axes[1, 0].plot(results[0]['energy_history'], 'r-', label='Enerji', linewidth=2)
        axes[1, 0].plot(results[0]['entropy_history'], 'b-', label='Entropi', linewidth=2)
        axes[1, 0].set_xlabel('Zaman Adimlari')
        axes[1, 0].set_ylabel('Degerler')
        axes[1, 0].set_title(f"{results[0]['scenario']} - Zaman Evrimi")
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)

    # 4. Yaşam olasılığı skorları
    life_scores = []
    for result in results:
        score = 0
        if result['avg_coherence'] > 0.35: score += 1
        if result['coherence_islands'] >= 2: score += 1
        if result['energy_entropy_correlation'] < -0.4: score += 1
        life_scores.append(score)

    colors = ['red' if s < 2 else 'orange' if s < 3 else 'green' for s in life_scores]
    axes[1, 1].bar(range(len(scenarios)), life_scores, color=colors, alpha=0.7)
    axes[1, 1].set_xlabel('Senaryolar')
    axes[1, 1].set_ylabel('Yasam Skoru (0-3)')
    axes[1, 1].set_title('CQON Yasam-Benzeri Organizasyon Skoru')
    axes[1, 1].set_xticks(range(len(scenarios)))
    axes[1, 1].set_xticklabels([s[:15] + '...' for s in scenarios], rotation=45)
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('realistic_cqon_analysis.png', dpi=200, bbox_inches='tight')
    plt.show()


def run_detailed_single_simulation():
    """Tek bir senaryoda detaylı analiz"""
    print("\n" + "=" * 60)
    print("🔍 TEK SENARYO DETAYLI ANALIZ - CQON MODEL")
    print("=" * 60)

    # Erken Dünya benzeri koşullar - OPTIMIZE EDILMIS
    sim = CQONSimulation(
        alpha=0.38, gamma=0.065, T=0.14, K0=0.95,  # Optimize parametreler
        grid_size=14, total_time=120, dt=0.15
    )

    print("📖 Senaryo: OPTIMIZE EDILMIS ERKEN DUNYA")
    print("   - Gelistirilmis rezonans hassasiyeti")
    print("   - Azaltilmis dekoherans")
    print("   - Optimize edilmis enerji akisi")
    print("   - CQON Teorisi: Enerji → Koherans → Enformasyon")
    print("\n⏳ CQON simülasyonu calisiyor...")

    results = sim.run(verbose=True)

    # Ek analiz
    if results:
        print(f"\n📈 DETAYLI ANALIZ:")
        print(f"   • Baslangic koherans: {results['coherence_history'][0]:.3f}")
        print(f"   • Maksimum koherans: {max(results['coherence_history']):.3f}")
        print(f"   • Koherans artisi: {results['coherence_history'][-1] - results['coherence_history'][0]:.3f}")
        print(f"   • Enerji kazanimi: {results['energy_history'][-1] - results['energy_history'][0]:.1f}")
        print(f"   • Entropi azalimi: {results['entropy_history'][0] - results['entropy_history'][-1]:.1f}")

        # Teori açıklaması
        print(f"\n📖 CQON TEORISI OZETI:")
        theory = results['theory_explanation']
        for key, value in theory.items():
            print(f"   • {key.replace('_', ' ').title()}: {value}")

    return results


if __name__ == "__main__":
    # Tüm senaryoları test et
    print("🚀 CQON Gercekci Test Baslatiliyor...")
    print("🎯 Model: Coherent Quantum Oscillator Network")
    all_results = realistic_parameter_sweep()

    # Detaylı tek senaryo analizi - OPTIMIZE ERKEN DUNYA
    detailed_results = run_detailed_single_simulation()

    # Görselleştirme
    if all_results:
        print("\n📊 Sonuclar görselleştiriliyor...")
        plot_comprehensive_results(all_results)

        print("\n✅ CQON GERCEKCI TEST TAMAMLANDI!")
        print("📁 'realistic_cqon_analysis.png' kaydedildi")

        # İstatistiksel özet
        successful_simulations = len(all_results)
        life_like_count = sum(1 for r in all_results if r.get('life_like_organization', False))
        print(f"📊 ISTATISTIK: {successful_simulations} simulasyon, {life_like_count} yasam-benzeri")

    else:
        print("\n❌ Test sonuc alinamadi!")