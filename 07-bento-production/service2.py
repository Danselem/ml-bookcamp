import bentoml

from bentoml.io import JSON
from bentoml.io import NumpyNdarray
import numpy as np

from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    country: str
    rating: float

#model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")
model_ref2 = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")
# second model mlzoomcamp_homework:jsi67fslz6txydu5"
#dv = model_ref.custom_objects["dictVectorizer"]
model_runner = model_ref2.to_runner()

svc = bentoml.Service("credit_risk_classifier", runners = [model_runner])

# @svc.api(input=JSON(pydantic_model = CreditApplication), output=JSON())
@svc.api(input=NumpyNdarray(shape=(-1, 4), dtype=np.float32, enforce_dtype=True, enforce_shape=True), output=JSON())
# @svc.api(input=JSON(), output=JSON())
async def classifier(vector):
#async def classifier(vector):
    # data = credit_application.dict()
    # vector = dv.transform(data)
    prediction = await model_runner.predict.async_run(vector)
    print(prediction)

    result = prediction[0]
    if result > 0.5:
        return {"status": "Declined"}
    elif result > 0.25:
        return {"status": "Maybe"}
    else:
        return {"status": "Approved"}