import re
import os

append = '''  <profiles>
    <profile>
        <id>instrument</id>
        <properties>
            <final.name>wsr-instrumented</final.name>
        </properties>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.codehaus.mojo</groupId>
                    <artifactId>cobertura-maven-plugin</artifactId>
                    <configuration>
                    </configuration>
                    <executions>
                        <execution>
                            <id>instrument-code</id>
                            <phase>process-classes</phase>
                            <goals>
                                <goal>instrument</goal>
                            </goals>
                        </execution>
                    </executions>
                </plugin>
                <plugin>
                    <artifactId>maven-source-plugin</artifactId>
                    <executions>
                        <execution>
                            <id>attach-sources</id>
                            <goals>
                                <goal>jar</goal>
                            </goals>
                        </execution>
                    </executions>
                    <inherited>true</inherited>
                </plugin>
            </plugins>
        </build>
    </profile>
  </profiles>
</project>
'''
with open('F:\Avi_OpenSource_CoadingPractise\PYTHON\FileEditing\pom.xml', "r+", encoding = "utf-8") as pom:
    pattern = "<goal>cobertura</goal>"
    rep = "<!-- <goal>cobertura</goal> -->"
    pomfile = pom.read()
    print(pomfile)
    print(type(pomfile))

    new = re.sub(pattern, rep, pomfile ,count=1)
    print(new)
    print(type(new))

    # comparision
    if pomfile is new:
        print('No substitution Done : Bad Luck')
    else:
        with open('F:\Avi_OpenSource_CoadingPractise\PYTHON\FileEditing\pom_new.xml', "w+", encoding = "utf-8") as pom_new:
            print('Substitution done')
    ##        print(pom.write(new))
            print('New pom file after savinf substitution')
            
            pom_new.write(new)
            data = pom_new.read()
            print(data)

# END
            
            
