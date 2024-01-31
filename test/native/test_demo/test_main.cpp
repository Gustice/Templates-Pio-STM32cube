#include <gtest/gtest.h>

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    if (RUN_ALL_TESTS())
        ;
    return 0;
}

TEST(Test, WillPass) {
    ASSERT_TRUE(true);
}

TEST(Test, WillFail) {
    ASSERT_TRUE(false);
}
