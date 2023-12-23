# 版权声明
# 2023 年 MT3 作者
#
# 根据 Apache 许可证 2.0 版（"许可证"）获得许可;
# 除非符合许可证的规定，否则您不能使用此文件。
# 您可以在以下网址获取许可证的副本：
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# 除非适用法律要求或书面同意，本软件是基于"按原样"的基础分发的，
# 没有任何明示或暗示的担保或条件。
# 有关特定语言的权限和限制，请参阅许可证。

"""事件的编码和解码。"""

import dataclasses
from typing import List, Tuple

# 事件范围数据类


@dataclasses.dataclass
class EventRange:
    type: str      # 事件类型
    min_value: int  # 最小值
    max_value: int  # 最大值

# 事件数据类


@dataclasses.dataclass
class Event:
    type: str  # 事件类型
    value: int  # 事件值

# 编码器类


class Codec:
    """对事件进行编码和解码。

    适用于声明词汇表的某些范围应用于令牌化之前或解码后的情况。
    此类旨在在使用 GenericTokenVocabulary 进行编码或解码之前从 Python 中使用。
    此类更轻量级，不包括 EOS 或 UNK 标记处理等功能。

    为了确保'shift'事件始终是词汇的第一个块，并从 0 开始，该事件类型是必需的并分别指定。
    """

    def __init__(self, max_shift_steps: int, steps_per_second: float,
                 event_ranges: List[EventRange]):
        """定义编码器。

        Args:
          max_shift_steps: 可以编码的最大移位步数。
          steps_per_second: 移位步数将被解释为持续时间为 1 / steps_per_second。
          event_ranges: 其他支持的事件类型及其范围。
        """
        self.steps_per_second = steps_per_second
        self._shift_range = EventRange(
            type='shift', min_value=0, max_value=max_shift_steps)
        self._event_ranges = [self._shift_range] + event_ranges
        # 确保所有事件类型都具有唯一名称。
        assert len(self._event_ranges) == len(
            set([er.type for er in self._event_ranges]))

    @property
    def num_classes(self) -> int:
        return sum(er.max_value - er.min_value + 1 for er in self._event_ranges)

    # 下面的几个方法是专为 'shift' 事件的简化特殊情况而设计的，
    # 旨在从 autograph 函数内部使用。

    def is_shift_event_index(self, index: int) -> bool:
        return (self._shift_range.min_value <= index) and (
            index <= self._shift_range.max_value)

    @property
    def max_shift_steps(self) -> int:
        return self._shift_range.max_value

    def encode_event(self, event: Event) -> int:
        """将事件编码为索引。"""
        offset = 0
        for er in self._event_ranges:
            if event.type == er.type:
                if not er.min_value <= event.value <= er.max_value:
                    raise ValueError(
                        f'事件值 {event.value} 不在类型 {event.type} 的有效范围内 [{er.min_value}, {er.max_value}]')
                return offset + event.value - er.min_value
            offset += er.max_value - er.min_value + 1

        raise ValueError(f'未知事件类型: {event.type}')

    def event_type_range(self, event_type: str) -> Tuple[int, int]:
        """返回事件类型的 [min_id, max_id]。"""
        offset = 0
        for er in self._event_ranges:
            if event_type == er.type:
                return offset, offset + (er.max_value - er.min_value)
            offset += er.max_value - er.min_value + 1

        raise ValueError(f'未知事件类型: {event_type}')

    def decode_event_index(self, index: int) -> Event:
        """将事件索引解码为事件。"""
        offset = 0
        for er in self._event_ranges:
            if offset <= index <= offset + er.max_value - er.min_value:
                return Event(
                    type=er.type, value=er.min_value + index - offset)
            offset += er.max_value - er.min_value + 1

        raise ValueError(f'未知事件索引: {index}')
