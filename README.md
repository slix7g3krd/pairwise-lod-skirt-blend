# pairwise-lod-skirt-blend

## 领域

游戏、图形与多媒体

## 主题

LOD 裙边融合

## 说明

裙边双端采样、属性按层归一与切换帧重建。

初始状态下 `render/lod_skirt_blend.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
