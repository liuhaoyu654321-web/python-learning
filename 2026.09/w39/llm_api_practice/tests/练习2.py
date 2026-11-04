
from pydantic import BaseModel, ValidationError


# 1. 定义数据规则
class AIResponse(BaseModel):
    summary: str
    urgent: bool
    confidence: float


# 2. 准备测试数据
data = {
    "summary": "数据库连接失败",
    "urgent": True,
    "confidence": 0.95
}


# 3. 尝试验证数据
try:
    result = AIResponse(**data)
    print("验证成功：", result)

# 4. 数据不符合规则时
except ValidationError as e:
    print("验证失败：")
    print(e)
