class DataValidator:

    @staticmethod
    def validate_dataframe(df):

        return {
            "row_count": int(len(df)),
            "column_count": int(len(df.columns)),
            "duplicate_count": int(df.duplicated().sum())
        }

    @staticmethod
    def schema_summary(df):

        schema = []

        for col in df.columns:

            schema.append({
                "column_name": col,
                "datatype": str(df[col].dtype),
                "null_count": int(df[col].isna().sum())
            })

        return schema
    
    def validate_business_rules(df):

        issues = {}

        if "age" in df.columns:
            issues["invalid_age"] = len(
                df[(df["age"] < 0) | (df["age"] > 120)]
            )

        if "bmi" in df.columns:
            issues["invalid_bmi"] = len(
                df[(df["bmi"] < 10) | (df["bmi"] > 100)]
            )

        return issues