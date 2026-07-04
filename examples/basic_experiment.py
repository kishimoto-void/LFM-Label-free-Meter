# LFM 使用例（Experiment内）

from LFM import LFM
from LFM.exporters.parquet_exporter import ParquetExporter  # TODO: 実装後
# from LFM.observers... import ...

# 初期化
lfm = LFM(version="0.1.0")

# 登録（デフォルト or 手動）
# registry = ObserverRegistry()
# for name, obs in registry.get_default().items():
#     lfm.register(name, obs)

lfm.register("velocity_stats", velocity_statistics)
lfm.register("topology_stats", topology_statistics)
# ... 追加

# シミュレーションループ例
max_steps = 10000
parquet_exporter = ParquetExporter()  # 仮

for step in range(max_steps):
    # physics.step(...)  # あなたのシミュレーション
    tick = step
    
    observations = lfm.measure_all(storage, tick)
    
    # Exporterで保存
    for obs in observations:
        # parquet_exporter.save(obs)  # 実装後
        pass

print(f"Completed {max_steps} steps with LFM observations.")
