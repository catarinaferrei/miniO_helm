from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "localhost:9000",
        access_key="minioUser",
        secret_key="minio123",
        secure= False,
    )

# Make 'testyaml' bucket if not exist.
    found = client.bucket_exists("testyaml")
    if not found:
        client.make_bucket("testyaml")
    else:
        print("Bucket 'test_aml' already exists")

    client.fput_object(
        "testyaml", "test.yaml", "path/to/file",
    )
    print(
        "'"path/to/file"' is successfully uploaded as "
        "object 'test.yaml' to bucket 'test.yaml'."
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
