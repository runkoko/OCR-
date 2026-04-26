# OCR-
光学字符识别（Optical Character Recognition, OCR）是指对文本材料的图像文件进行分析识别处理，以获取文字和版本信息的过程。也就是说将图象中的文字进行识别，并返回文本形式的内容。
# 注意
移动端的超轻量模型：超轻量ppocr_mobile移动端系列：检测（2.6M）+方向分类器（0.9M）+ 识别（4.6M）= 8.1M，仅有8.1M。chinese_ocr_db_crnn_mobile（1.1.0最新版）。

服务器端的精度更高模型：识别精度更高，chinese_ocr_db_crnn_server。

该 Module 用于识别图片当中的汉字、数字、字母。如果仅需要检测，也可单独使用chinese_text_detection_db_server或者chinese_text_detection_db_mobile得到检测结果的文本框

开发者可以基于PaddleHub提供的OCR中文识别Module，实现一键文字识别，适用于常见的OCR应用场景中。
